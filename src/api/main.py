from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import (
    auth_routes,
    user_routes,
    spb_routes,
    orders_routes,
    trends_routes,
    assets_routes,
)

from .routes_config import URL_PREFIX, API_DOC, API_DOC_REDOC, API_DOC_JSON, API_VERSION


def create_app():
    app = FastAPI(
        title="Toro - Backend",
        description="API da plataforma",
        openapi_url=API_DOC_JSON,
        redoc_url=API_DOC_REDOC,
        docs_url=API_DOC,
        version=API_VERSION,
    )

    app.include_router(user_routes, prefix=f"{URL_PREFIX}/users", tags=["Users"])
    app.include_router(auth_routes, prefix=f"{URL_PREFIX}/auth", tags=["Auth"])
    app.include_router(spb_routes, prefix=f"{URL_PREFIX}/spb", tags=["SPB"])
    app.include_router(orders_routes, prefix=f"{URL_PREFIX}/order", tags=["Orders"])
    app.include_router(trends_routes, prefix=f"{URL_PREFIX}/trends", tags=["Trends"])
    app.include_router(assets_routes, prefix=f"{URL_PREFIX}/assets", tags=["Assets"])

    return app


app = create_app()


origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(f"{URL_PREFIX}/info", summary="links da documentacao da API", tags=["info"])
def read_root():  # pragma: no cover
    return {"doc": API_DOC, "redoc": API_DOC_REDOC, "json": API_DOC_JSON}
