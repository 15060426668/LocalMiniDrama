const http = require("node:http");

const originalCreateServer = http.createServer;
http.createServer = function patchedCreateServer(...args) {
  if (typeof args[0] === "function") {
    const originalHandler = args[0];
    args[0] = (request, response) => {
      const originalWriteHead = response.writeHead.bind(response);
      response.writeHead = (statusCode, headers = {}) => originalWriteHead(statusCode, {
        ...headers,
        "Cache-Control": "no-store, no-cache, must-revalidate",
        Expires: "0",
        Pragma: "no-cache",
      });
      originalHandler(request, response);
    };
  }
  return originalCreateServer.apply(http, args);
};

require("./extract_transition_frames_http.cjs");
