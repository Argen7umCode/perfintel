from abc import abstractmethod

from repositories.abstract import AbstractRepository
from schemas.user import User


class AbstractUserRepository(AbstractRepository):
    
    @abstractmethod
    async def get(self, id: int) -> list[User]:
        pass

    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def update(self, user: User) -> None:
        pass

class AsyncPGUserRepository(AbstractUserRepository):

    async def get(self, id: int) -> list[User]:
        conn = await self._get_connection()
        res = await conn.fetch("SELECT * FROM users WHERE id = $1", id)
        await conn.close()
        return [User(**r) for r in res]

    async def save(self, user: User) -> None:
        conn = await self._get_connection()
        await conn.execute("INSERT INTO users (name) VALUES ($1)", user.name)
        await conn.close()

    async def delete(self, id: int) -> None:
        conn = await self._get_connection()
        await conn.execute("DELETE FROM users WHERE id = $1", id)
        await conn.close()

    async def update(self, user: User) -> None:
        conn = await self._get_connection()
        await conn.execute("UPDATE users SET name = $1 WHERE id = $2", user.name, user.id)
        await conn.close()