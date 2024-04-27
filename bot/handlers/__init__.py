from aiogram import Router


def get_handlers_router() -> Router:
    from . import start, manage, admin, upload

    router = Router()
    router.include_router(start.router)
    router.include_router(manage.router)
    router.include_router(admin.router)
    router.include_router(upload.router)

    return router
