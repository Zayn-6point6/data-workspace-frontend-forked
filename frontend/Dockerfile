FROM node:latest
EXPOSE 3000

COPY ./dataworkspace/dataworkspace/static/js/react_apps /frontend
WORKDIR /frontend
RUN npm install --no-progress --ignore-optional
CMD ["npm", "run", "dev"]
