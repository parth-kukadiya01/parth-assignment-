import uvicorn
from app.routes import user, project
from fastapi.middleware.cors import CORSMiddleware
from app.core.logger import logger
from app.database.database import create_db_and_tables
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(
        title="Project Management System",
        description="A RESTful API with JWT Authentication and RBAC",
        version="1.0.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user.router, prefix="", tags=["Users"])
    app.include_router(project.router, prefix="/projects", tags=["Projects"])

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()
        logger.info("Database tables created.")

    return app


app = create_app()
