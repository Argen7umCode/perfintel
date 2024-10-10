from abc import ABC, abstractmethod
import asyncpg

from schemas.abstract import Schema


class AbstractRepository(ABC):
    @abstractmethod
    async def get(self, id: int) -> list[Schema]:
        pass

    @abstractmethod
    async def save(self, object: Schema) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def update(self, object: Schema) -> None:
        pass

class AsyncPGRepository(AbstractRepository):

    def _get_connection(self) -> asyncpg.Connection:
        return asyncpg.connect()


    async def get(self, id: int) -> list[Schema]:
        pass

    @abstractmethod
    async def save(self, object: Schema) -> None:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass

    @abstractmethod
    async def update(self, object: Schema) -> None:
        pass