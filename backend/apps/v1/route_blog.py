from fastapi import APIRouter, Depends, Form, Request, responses, status
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.apis.v1.route_login import get_current_user
# from backend.db.models.user import User
from backend.db.repository.blog import create_new_blog  # update_blog,
from backend.db.repository.blog import delete_blog, list_blogs, retreive_blog
from backend.db.session import get_db
from backend.schemas.blog import CreateBlog

templates = Jinja2Templates(directory="backend/templates")
router = APIRouter()


@router.get("/")
def home(
    request: Request,
    alert: str | None = None,
    db: Session = Depends(get_db),
):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "blog/home.html", {"request": request, "blogs": blogs, "alert": alert}
    )


@router.get("/app/blog/{id}")
def blog_detail(request: Request, id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    return templates.TemplateResponse(
        "blog/detail.html", {"request": request, "blog": blog}
    )


@router.get("/app/create-new-blog")
def create_blog(request: Request):
    return templates.TemplateResponse(
        "blog/create_blog.html",
        {"request": request},
    )


@router.post("/app/create-new-blog")
def create_blog(  # noqa: F811
    request: Request,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
    # current_user: User = Depends(get_current_user),
):
    token = request.cookies.get("access_token")
    _, token = get_authorization_scheme_param(token)
    print("hello")
    try:
        author = get_current_user(token=token, db=db)
        blog = CreateBlog(title=title, content=content)
        blog = create_new_blog(blog=blog, db=db, author_id=author.id)
        return responses.RedirectResponse(
            "/?alert=Blog Submitted for Review",
            status_code=status.HTTP_302_FOUND,
        )
    except Exception as e:
        errors = ["Please log in to create blog"]
        print("Exception raised", e)
        return templates.TemplateResponse(
            "blog/create_blog.html",
            {
                "request": request,
                "errors": errors,
                "title": title,
                "content": content,
            },
        )


# @router.put('/blog/{id}', response_model=ShowBlog)
# def update_a_blog(
#     request: Request,
#     id: int,
#     blog: UpdateBlog,
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user),
# ):
#     token = request.cookies.get("access_token")
#     _, token = get_authorization_scheme_param(token)
#     try:
#         author = get_current_user(token=token, db=db)
#         msg = update_blog(id=id, blog, author_id=current_user.id, db)
#         alert = msg.get("error") or msg.get("msg")
#         return responses.RedirectResponse(
#             f"/?alert={alert}", status_code=status.HTTP_302_FOUND
#         )
#     except Exception as e:
#         print(f"Exception raised while deleting {e}")
#         blog = retreive_blog(id=id, db=db)
#         return templates.TemplateResponse(
#             "blog/detail.html",
#            {"request": request,
#             "alert": "Please Login Again",
#              "blog": blog,
#            }
#         )


@router.get("/delete/{id}")
def delete_a_blog(request: Request, id: int, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    _, token = get_authorization_scheme_param(token)
    try:
        author = get_current_user(token=token, db=db)
        msg = delete_blog(id=id, author_id=author.id, db=db)
        alert = msg.get("error") or msg.get("msg")
        return responses.RedirectResponse(
            f"/?alert={alert}", status_code=status.HTTP_302_FOUND
        )
    except Exception as e:
        print(f"Exception raised while deleting {e}")
        blog = retreive_blog(id=id, db=db)
        return templates.TemplateResponse(
            "blog/detail.html",
            {"request": request, "alert": "Please Login Again", "blog": blog},
        )
