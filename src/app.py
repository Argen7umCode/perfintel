import asyncio
import logging
from typing import Sequence

from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode

import config
from loader import dp
from handlers import routers



class App:
    
    def __init__(
        self, 
        token: str, 
        dp: Dispatcher
    ) -> None:
        self.bot = Bot(token=token)
        self.dp = dp

    def include_routers(
        self, 
        routers: Sequence[Router]
    ) -> None:
        for router in routers:
            self.dp.include_router(router)

    async def startup_bot(
        self, 
        *args, 
        **kwargs
    ) -> None:
        self.include_routers(kwargs.get('routers', []))
        await self.bot.delete_webhook(drop_pending_updates=True)
        await self.dp.start_polling(
            self.bot,
            allowed_updates=dp.resolve_used_update_types()
        )


async def main():
    app = App(token=config.BOT_TOKEN, dp=dp)
    await app.startup_bot(routers=routers)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())