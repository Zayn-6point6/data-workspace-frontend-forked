import asyncio
import logging
import os
import sys

import aiopg
from aiohttp import web
import psycopg2.sql
from arango import ArangoClient


async def async_main():
    stdout_handler = logging.StreamHandler(sys.stdout)
    for logger_name in ["aiohttp.server", "aiohttp.web", "aiohttp.access"]:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(stdout_handler)

    async def handle_stop(_):
        sys.exit()

    async def handle_dataset(request):
        database = request.match_info["database"]
        table = request.match_info["table"]
        dsn = os.environ[f"DATABASE_DSN__{database}"]
        async with aiopg.create_pool(dsn) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute(
                        psycopg2.sql.SQL("SELECT * FROM {}").format(psycopg2.sql.Identifier(table))
                    )
                    rows = [row[0] for row in await cur.fetchall()]

        return web.json_response({"data": rows}, status=200)

    async def handle_post_schema_table(request):
        database = request.match_info["database"]
        schema = request.match_info["schema"]
        table = request.match_info["table"]
        dsn = os.environ[f"DATABASE_DSN__{database}"]

        async with aiopg.create_pool(dsn) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute(
                        psycopg2.sql.SQL(
                            """
                            CREATE TABLE {}.{} (
                                id          SERIAL PRIMARY KEY,
                                colour      varchar(40) NOT NULL
                            );
                        """
                        ).format(
                            psycopg2.sql.Identifier(schema),
                            psycopg2.sql.Identifier(table),
                        )
                    )
                    await cur.execute(
                        psycopg2.sql.SQL(
                            """
                        INSERT INTO {}.{} (colour) VALUES('orange')
                    """
                        ).format(
                            psycopg2.sql.Identifier(schema),
                            psycopg2.sql.Identifier(table),
                        )
                    )

        return web.json_response(status=200)

    async def handle_get_schema_table(request):
        database = request.match_info["database"]
        schema = request.match_info["schema"]
        table = request.match_info["table"]
        dsn = os.environ[f"DATABASE_DSN__{database}"]
        async with aiopg.create_pool(dsn) as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute(
                        psycopg2.sql.SQL("SELECT * FROM {}.{}").format(
                            psycopg2.sql.Identifier(schema),
                            psycopg2.sql.Identifier(table),
                        )
                    )
                    rows = await cur.fetchall()

        return web.json_response({"data": rows}, status=200)

    async def handle_get_graph_collection(request):
        # Get temporary user credentials
        arango_user = os.environ["ARANGO_USER"]
        arango_password = os.environ["ARANGO_PASSWORD"]
        arango_host = os.environ["ARANGO_HOST"]
        arango_port = os.environ["ARANGO_PORT"]

        # Connect to ArangoDB with temporary credentials
        client = ArangoClient(hosts=f"http://{arango_host}:{arango_port}")
        db = client.db("Datasets", username=arango_user, password=arango_password)

        testcollection1 = db.collection("testcollection1").properties()
        try:
            testcollection2 = db.collection("testcollection2").properties()
        except Exception as collection_access_exception:  # pylint: disable=broad-except
            testcollection2 = (
                collection_access_exception.error_message
            )  # pylint: disable=no-member

        data = {
            "testcollection1": testcollection1,
            "testcollection2": testcollection2,
        }
        return web.json_response({"data": data}, status=200)

    upstream = web.Application()
    upstream.add_routes([web.post("/stop", handle_stop)])
    upstream.add_routes([web.get("/arango", handle_get_graph_collection)])
    upstream.add_routes([web.get("/{database}/{table}", handle_dataset)])
    upstream.add_routes([web.get("/{database}/{schema}/{table}", handle_get_schema_table)])
    upstream.add_routes([web.post("/{database}/{schema}/{table}", handle_post_schema_table)])
    upstream_runner = web.AppRunner(upstream)
    await upstream_runner.setup()
    upstream_site = web.TCPSite(upstream_runner, "0.0.0.0", 8888)
    await upstream_site.start()
    await asyncio.Future()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())


if __name__ == "__main__":
    main()
