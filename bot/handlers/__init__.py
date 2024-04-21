from aiogram import Router


def get_handlers_router() -> Router:
    from . import start, admin

    router = Router()
    router.include_router(start.router)
    router.include_router(admin.router)

    return router
