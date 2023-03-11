import uvicorn
from fastapi import FastAPI
from app.api.routes.api import router as api_router
from fastapi_pagination import add_pagination
from app.db.events import create_start_app_handler, create_stop_app_handler

def get_application() -> FastAPI:
    """
    Initialize the application (port 8000) and connects to DB at the startup.
    Failure to connect to DB doesn't bring up the application.
    It does gracefully shuts down when the application closes.

    Returns:
        FastAPI: Fast API App.
    """
    application = FastAPI(title="Gutenberg Demo", debug=False, version=0.1)

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(api_router)
    add_pagination(application)

    return application

app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)