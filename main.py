
# Q1 :

from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/ping", response_class=Response)
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)
# # Q2 : 
# from fastapi.responses import HTMLResponse

# @app.get("/home")
# def home():
#     html_content = "<html><body><h1>Welcome home!</h1></body></html>"
#     return HTMLResponse(content=html_content, status_code=200)

# # Q3 :
# from fastapi.requests import Request
# from fastapi.responses import HTMLResponse
# from fastapi.exception_handlers import http_exception_handler
# from fastapi.exceptions import RequestValidationError
# from starlette.exceptions import HTTPException as StarletteHTTPException

# @app.exception_handler(StarletteHTTPException)
# async def custom_404_handler(request: Request, exc: StarletteHTTPException):
#     if exc.status_code == 404:
#         return HTMLResponse("<h1>404 NOT FOUND</h1>", status_code=404)
#     return await http_exception_handler(request, exc)

# # Q4 :
# from pydantic import BaseModel
# from datetime import datetime
# from fastapi import status

# posts = []

# class Post(BaseModel):
#     author: str
#     title: str
#     content: str
#     creation_datetime: datetime

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def add_posts(new_posts: list[Post]):
#     posts.extend(new_posts)
#     return posts

# # Q5 :
# @app.get("/posts")
# def get_posts():
#     return posts

# # Q6 :
# @app.put("/posts")
# def update_post(post_data: Post):
#     for i, post in enumerate(posts):
#         if post.title == post_data.title:
#             posts[i] = post_data
#             return posts
#     posts.append(post_data)
#     return posts

# # Bonus :
# from fastapi import Header, HTTPException
# import base64

# @app.get("/ping/auth")
# def ping_auth(authorization: str = Header(None)):
#     if authorization is None or not authorization.startswith("Basic "):
#         raise HTTPException(status_code=401, detail="Unauthorized")

#     encoded = authorization.split(" ")[1]
#     decoded_bytes = base64.b64decode(encoded)
#     decoded = decoded_bytes.decode("utf-8")
#     username, password = decoded.split(":")

#     if username == "admin" and password == "123456":
#         return Response(content="pong", media_type="text/plain")
    
#     raise HTTPException(status_code=401, detail="Invalid credentials")
