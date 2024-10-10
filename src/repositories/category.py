from abc import abstractmethod

from repositories.abstract import AbstractRepository
from schemas.category import Category


class AbstractCategoryRepository(AbstractRepository):
    
    @abstractmethod
    async def get(self, id: int) -> list[Category]:
        pass

    @abstractmethod
    async def save(self, category: Category) -> None:
        pass

    @abstractmethod
    async def update(self, category: Category) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass


class AsyncPGCategoryRepository(AbstractCategoryRepository):

    async def get(self, id: int) -> list[Category]:
        conn = await self._get_connection()
        res = await conn.fetch("SELECT * FROM categories WHERE id = $1", id)
        await conn.close()
        return [Category(**r) for r in res]

    async def save(self, category: Category) -> None:
        conn = await self._get_connection()
        await conn.execute("INSERT INTO categories (name, user_id) VALUES ($1, $2)", category.name, category.user_id)
        await conn.close()

    async def update(self, category: Category) -> None:
        conn = await self._get_connection()
        await conn.execute("UPDATE categories SET name = $1 WHERE id = $2", category.name, category.id)
        await conn.close()

    async def delete(self, id: int) -> None:
        conn = await self._get_connection()
        await conn.execute("DELETE FROM categories WHERE id = $1", id)
        await conn.close()