from fastapi import FastAPI
from bloc.db import init
from bloc.publications.routers import router as publication_router
from bloc.users.routers import auth_router, register_router, password_reset_router


app = FastAPI(title="MDBloc API")


app.add_event_handler("startup", init)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(publication_router)
app.include_router(auth_router, prefix="/auth/jwt", tags=["auth"])
app.include_router(register_router, prefix="/auth", tags=["auth"])
app.include_router(password_reset_router, prefix="/auth", tags=["auth"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
