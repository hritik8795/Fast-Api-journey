from db.database import AsyncSessionLocal
from typing import AsyncGenerator


async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        yield session
