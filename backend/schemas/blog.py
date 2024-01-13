from pydantic import BaseModel


class CreateBlog(BaseModel):
    title: str
    content: str | None = None


class ShowBlog(BaseModel):
    title: str
    content: str | None

    class Config:
        from_attributes = True


class UpdateBlog(CreateBlog):
    ...
