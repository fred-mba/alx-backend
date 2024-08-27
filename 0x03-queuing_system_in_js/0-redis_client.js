import { createClient } from "redis";

/**
 * Should connect to the Redis server running on your machine:
 * `Redis client connected to the server` when the connection to Redis works correctly
 * `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work
 */
const client = createClient();

client.on('connect', (stream) => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err.message}`);s
});
