resource "aws_ecs_task_definition" "pgweb" {
  family                = "${var.prefix}-pgweb"
  container_definitions = "${data.template_file.pgweb_container_definitions.rendered}"
  execution_role_arn    = "${aws_iam_role.notebook_task_execution.arn}"
  # task_role_arn         = "${aws_iam_role.notebook_task.arn}"
  network_mode          = "awsvpc"
  cpu                   = "${local.notebook_container_cpu}"
  memory                = "${local.notebook_container_memory}"
  requires_compatibilities = ["FARGATE"]

  volume {
    name = "home_directory"
  }

  lifecycle {
    ignore_changes = [
      "revision",
    ]
  }
}

data "external" "pgweb_current_tag" {
  program = ["${path.module}/task_definition_tag.sh"]

  query = {
    task_family = "${var.prefix}-pgweb"
    container_name = "${local.notebook_container_name}"
  }
}

data "external" "pgweb_metrics_current_tag" {
  program = ["${path.module}/task_definition_tag.sh"]

  query = {
    task_family = "${var.prefix}-pgweb"
    container_name = "metrics"
  }
}

data "external" "pgweb_s3sync_current_tag" {
  program = ["${path.module}/task_definition_tag.sh"]

  query = {
    task_family = "${var.prefix}-pgweb"
    container_name = "s3sync"
  }
}

data "template_file" "pgweb_container_definitions" {
  template = "${file("${path.module}/ecs_notebooks_notebook_container_definitions.json")}"

  vars = {
    container_image  = "${var.pgweb_container_image}:pgweb-spike"
    container_name   = "${local.notebook_container_name}"

    log_group  = "${aws_cloudwatch_log_group.notebook.name}"
    log_region = "${data.aws_region.aws_region.name}"

    sentry_dsn = "${var.sentry_notebooks_dsn}"
    sentry_environment = "${var.sentry_environment}"

    metrics_container_image = "${aws_ecr_repository.metrics.repository_url}:master"
    s3sync_container_image = "${aws_ecr_repository.s3sync.repository_url}:master"

    home_directory = "/home/jovyan"
  }
}
