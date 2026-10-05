from typing import List, Optional
from sqlmodel import SQLModel

class CategoryBase(SQLModel):
    pass

class CategoryCreate(CategoryBase):
    pass

class CategoryPublic(CategoryBase):
    pass


class UserBase(SQLModel):
    pass

class ReviewBase(SQLModel):
    pass


class ReviewPublic(ReviewBase):
    pass


class ProductBase(SQLModel):
    name : str
    price : float
    description : str


class ProductCreate(ProductBase):
    category_id : int

class ProductPublic(ProductBase):
    id : int
    category: CategoryPublic
    review : List[ReviewPublic] = []
