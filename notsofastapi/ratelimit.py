import time
import threading
from functools import wraps
from fastapi import HTTPException, Request

class RateLimiter:
    def __init__(self):
        self.requests = {}
        self.lock = threading.Lock()

    def is_allowed(self, client_ip: str, limit: int, period: int) -> bool:
        now = time.monotonic()

        with self.lock:
            if client_ip not in self.requests:
                self.requests[client_ip] = []

            self.requests[client_ip] = [t for t in self.requests[client_ip] if now - t < period]

            if len(self.requests[client_ip]) >= limit:
                return False

            self.requests[client_ip].append(now)
            return True

limiter = RateLimiter()

def ratelimit(limit: int = 5, period: int = 60):
    """
    Rate-limiting decorator for FastAPI.

    :param limit: Maximum number of requests allowed in the period.
    :param period: Time window in seconds.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            client_ip = request.client.host

            if not limiter.is_allowed(client_ip, limit, period):
                raise HTTPException(status_code=429, detail="Rate limit exceeded")

            return await func(request, *args, **kwargs)

        return wrapper
    return decorator