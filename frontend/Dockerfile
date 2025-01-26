FROM node:22-alpine AS builder

ENV NODE_ENV=production
ENV APP_DIR=/app

WORKDIR $APP_DIR

COPY package*.json ./

RUN npm install

COPY . .

RUN npx vite build

FROM node:22-alpine as production

ENV NODE_ENV=production
ENV APP_DIR=/app
ENV PORT=3000

WORKDIR $APP_DIR

COPY --from=builder $APP_DIR/build ./build

EXPOSE $PORT

CMD ["node", "build"]