const http = require("node:http");

const originalCreateServer = http.createServer;
let pageVersion = 0;

http.createServer = function patchedCreateServer(...args) {
  if (typeof args[0] === "function") {
    const originalHandler = args[0];
    args[0] = (request, response) => {
      const requestedUrl = request.url || "";
      if (requestedUrl === "/") {
        pageVersion += 1;
        const originalEnd = response.end.bind(response);
        response.end = (body, ...endArgs) => {
          const rewritten = typeof body === "string"
            ? body.replace("/video.mp4", `/video.mp4?v=${pageVersion}`)
            : body;
          return originalEnd(rewritten, ...endArgs);
        };
      } else if (requestedUrl.startsWith("/video.mp4?")) {
        request.url = "/video.mp4";
      }

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
