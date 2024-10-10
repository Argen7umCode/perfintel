from abc import abstractmethod

from repositories.abstract import AbstractRepository
from schemas.record import Record


class AbstractRecordRepository(AbstractRepository):

    @abstractmethod
    async def get(self, id: int) -> list[Record]:
        pass

    @abstractmethod
    async def save(self, record: dict) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def update(self, record: dict) -> None:
        pass


class AsyncPGRecordRepository(AbstractRecordRepository):

    async def get(self, id: int) -> list[Record]:
        conn = await self._get_connection()
        res = await conn.fetch("SELECT * FROM records WHERE id = $1", id)
        await conn.close()
        return [Record(**r) for r in res]

    async def save(self, record: dict) -> None:
        conn = await self._get_connection()
        await conn.execute("INSERT INTO records (name) VALUES ($1)", record['name'])
        await conn.close()

    async def delete(self, id: int) -> None:
        conn = await self._get_connection()
        await conn.execute("DELETE FROM records WHERE id = $1", id)
        await conn.close()

    async def update(self, record: dict) -> None:
        conn = await self._get_connection()
        await conn.execute("UPDATE records SET name = $1 WHERE id = $2", record['name'], record['id'])
        await conn.close()