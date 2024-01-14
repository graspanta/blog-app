import json

from fastapi import APIRouter, Depends, Form, Request, responses, status
from fastapi.templating import Jinja2Templates
from pydantic.error_wrappers import ValidationError
from sqlalchemy.orm import Session

from backend.apis.v1.route_login import authenticate_user
from backend.core.security import create_access_token
from backend.db.repository.user import create_new_user
from backend.db.session import get_db
from backend.schemas.user import UserCreate

templates = Jinja2Templates(directory="backend/templates")
router = APIRouter()


@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse(
        "auth/register.html", {"request": request}
    )  # noqa: E501


@router.post("/register")
def register(  # noqa: F811
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    errors = []
    try:
        user = UserCreate(email=email, password=password)
        create_new_user(user=user, db=db)
        return responses.RedirectResponse(
            "/?alert=登録に成功しました",
            status_code=status.HTTP_302_FOUND,  # noqa: E501
        )
    except ValidationError as e:
        errors_list = json.loads(e.json())
        for item in errors_list:
            errors.append(item.get("loc")[0] + ": " + item.get("msg"))
        return templates.TemplateResponse(
            "auth/register.html", {"request": request, "errors": errors}
        )


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.post("/login")
def login(  # noqa: F811
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    errors = []
    user = authenticate_user(email=email, password=password, db=db)
    if not user:
        errors.append("Incorrect email or password")
        return templates.TemplateResponse(
            "auth/login.html", {"request": request, "errors": errors}
        )
    access_token = create_access_token(data={"sub": email})
    response = responses.RedirectResponse(
        "/?alert=ログインに成功しました", status_code=status.HTTP_302_FOUND
    )
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return response
