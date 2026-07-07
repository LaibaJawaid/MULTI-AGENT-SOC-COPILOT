"""
Request Logging Middleware

Logs every API request.

Useful for production debugging.
"""

import time

from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.time()

        response = await call_next(request)

        duration = round(time.time() - start, 3)

        print(
            f"[{request.method}] "
            f"{request.url.path} "
            f"{duration}s"
        )

        return response