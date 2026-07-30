#fastapi
from fastapi import FastAPI
#routes
from src.router.book import router as book
from src.router.user import router as user
from src.router.favorite import router as favorite

#route
app = FastAPI()

app.include_router(book)
app.include_router(user)
app.include_router(favorite)