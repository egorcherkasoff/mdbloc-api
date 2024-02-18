from fastapi import FastAPI
from bloc.db import init
from bloc.views import publication_router


app = FastAPI(title="MDBloc API")


app.add_event_handler("startup", init)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(publication_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
