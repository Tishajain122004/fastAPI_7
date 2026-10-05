#this code create the object that actually manages db connection and transactions 
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.orm import sessionmaker
from .config import settings

#create_async_engine - creates connection pool 
engine = create_async_engine(settings.DATABASE_URL, echo=True)

#session - query the data from db
#why factory - instead of new sesion every time we create factory, whenever we need a session, we call asyncsessionfactory and it will produce a perfectly configured session that is already linked to engine
AsyncSessionFactory  = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session():
    async with AsyncSessionFactory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
        finally:
            await session.close()
