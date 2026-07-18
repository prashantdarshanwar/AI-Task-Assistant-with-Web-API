"""
Request Logging Middleware
"""

import logging
import time

from starlette.middleware.base import BaseHTTPMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("AI-Task-Assistant")


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request,
        call_next,
    ):

        start = time.time()

        logger.info(
            "%s %s",
            request.method,
            request.url.path,
        )

        response = await call_next(request)

        process_time = round(
            time.time() - start,
            3,
        )

        logger.info(
            "%s completed in %s sec",
            request.url.path,
            process_time,
        )

        return response