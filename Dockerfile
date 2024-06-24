FROM --platform=linux/amd64 node:21-alpine AS base

FROM base AS deps

WORKDIR /app

COPY package.json yarn.lock* package-lock.json*  ./

RUN \
    if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
    elif [ -f package-lock.json ]; then npm ci; \
    else echo "Lockfile not found." && exit 1; \
    fi

FROM base AS builder

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY . .

RUN yarn build

FROM base AS runner

WORKDIR /app

ENV NODE_ENV production

RUN addgroup --system --gid 1001 aws-test \
    && adduser --system --uid 101 user

COPY --from=builder --chown=user:aws-test /app/node_modules/ ./node_modules/
COPY --from=builder --chown=user:aws-test /app/dist/ ./dist/

USER user

EXPOSE 4000

# Command to run the application
CMD ["node", "dist/main.js"]