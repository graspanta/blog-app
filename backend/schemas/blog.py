# from datetime import date

from pydantic import BaseModel, validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str | None = None

    @validator("slug", pre=True)
    def generate_slug(cls, slug, values):
        title = values.get("title")
        slug = None
        if title:
            slug = title.replace(" ", "-").lower()
        return slug


class ShowBlog(BaseModel):
    title: str
    content: str | None
    # created_at: date

    class Config:
        from_attributes = True


class UpdateBlog(CreateBlog):
    ...
