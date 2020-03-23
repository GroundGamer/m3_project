from django.conf.urls import url
from objectpack import desktop
from app.controller import controller
from app.actions import UserPack, ContentTypePack, GroupPack, PermissionPack


def register_urlpatterns():

    """
    Регистрация конфигурации урлов для приложения
    """

    return [url(*controller.urlpattern)]


def register_actions():

    """
    Регистрация экшен-паков
    """

    return controller.packs.extend([
        # YourActionPack()
        UserPack(),
        ContentTypePack(),
        GroupPack(),
        PermissionPack(),
       ])


def register_desktop_menu():

    """
    регистрация элементов рабочего стола
    """

    desktop.uificate_the_controller(
       controller,
       menu_root=desktop.Desktop()
    )
