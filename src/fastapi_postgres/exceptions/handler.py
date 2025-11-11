from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastapi_postgres.exceptions.math import *


def set_error_handlers(app: FastAPI):
    @app.exception_handler(MultiplicationError)
    async def multplication_exception_handler(
        request: Request, exc: MultiplicationError
    ):
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "type": exc.__class__.__name__,
                    "message": str(exc),
                    "context": str(exc.__context__),
                }
            },
        )
