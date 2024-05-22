from pydantic import BaseModel, conint


class PostBase(BaseModel):
    id: conint(strict=True, gt=0)


class PostProperty(BaseModel):
    title: str
    body: str


class PostResponse(PostBase, PostProperty):
    userId: conint(strict=True, gt=0)


class PostUpdateResponse(PostResponse):
    title: str = None
    body: str = None
