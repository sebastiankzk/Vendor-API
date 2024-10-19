from fastapi import FastAPI, HTTPException
from app.models import vendor_profile
# from fastapi.middleware.cors import CORSMiddleware
# import uvicorn

# from app.route import vendor_user_router

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(vendor_user_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# if __name__ == "__main__":
#     uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)
