FROM node:22-alpine AS builder
ENV APP_DIR=/app
ENV API_PATH="https://parkpappa-api.cloud.spetsen.net"

WORKDIR $APP_DIR
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
RUN npm prune --production

FROM node:22-alpine AS production
ENV APP_DIR=/app
ENV PORT=3000

WORKDIR $APP_DIR
COPY --from=builder $APP_DIR/build build/
COPY --from=builder $APP_DIR/node_modules node_modules/
COPY package.json .

EXPOSE $PORT

ENV NODE_ENV=production
CMD ["node", "build"]