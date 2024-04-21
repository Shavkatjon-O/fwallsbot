from aiogram import Dispatcher


def register_middlewares(dp: Dispatcher) -> None:
    from .auth import AuthMiddleware
    from .album import AlbumMiddleware

    dp.message.outer_middleware(AuthMiddleware())
    dp.message.middleware(AlbumMiddleware())
