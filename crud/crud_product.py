from typing import List
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from model.models import product
from schema import ProductCreate

async def create_product(product_data : ProductCreate, session: AsyncSession)->product:
    db_product = product.model_validate(product_data)
    session.add(db_product)
    await session.commit()
    await session.refresh(db_product)
    return db_product

async def get_all_products(session : AsyncSession)-> List[product]:
    statement = select(product)
    result = await session.exec(statement)
    return result.all()

async def get_product_by_id(product_id : int, session : AsyncSession)-> product:
    statement = select(product).where[product_id == product_id]
    result = await session.exec(statement)
    return result.one_or_none()




