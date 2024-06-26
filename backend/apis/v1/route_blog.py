from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.apis.v1.route_login import get_current_user
from backend.db.models.user import User
from backend.db.repository.blog import (
    create_new_blog,
    delete_blog,
    list_blogs,
    retreive_blog,
    update_blog,
)
from backend.db.session import get_db
from backend.schemas.blog import CreateBlog, ShowBlog, UpdateBlog

router = APIRouter()


@router.post(
    "/blog", response_model=ShowBlog, status_code=status.HTTP_201_CREATED
)  # noqa: E501
def create_blog(
    blog: CreateBlog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    blog = create_new_blog(blog=blog, db=db, author_id=current_user.id)
    return blog


@router.get("/blog/{id}", response_model=ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            detail=f"{id}番のブログが存在しません",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.get("/blogs", response_model=list[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs


@router.put("/update/{id}", response_model=ShowBlog)
def update_a_blog(
    id: int,
    blog: UpdateBlog,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    blog = update_blog(id=id, blog=blog, author_id=current_user.id, db=db)
    if isinstance(blog, dict):
        raise HTTPException(
            detail=blog.get("error"),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return blog


@router.delete("/delete/{id}")
def delete_a_blog(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    message = delete_blog(id=id, author_id=current_user.id, db=db)
    if not User:
        raise HTTPException(
            detail=message.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"),
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    return {"msg": f"{id}番のブログの削除に成功しました"}
