from aiogram import Router


def get_handlers_router() -> Router:
    from . import start, manage, admin

    router = Router()
    router.include_router(start.router)
    router.include_router(manage.router)
    router.include_router(admin.router)

    return router
