from fastapi import FastAPI
from app.routes import profile, skills, status  #projects, 


app = FastAPI(title="Aaron's GitHub API")

#TODO: Add the routers for the different endpoints
app.include_router(profile.router)
app.include_router(skills.router)
#app.include_router(projects.router)
app.include_router(status.router)

@app.get("/")
def root():
    return {"message": "Welcome to Aaron's GitHub API"}

@app.get("/health")
def health():
    return {"status": "ok"}