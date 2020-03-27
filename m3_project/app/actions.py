from objectpack.actions import ObjectPack
from objectpack.observer import Observer
from objectpack.ui import ModelEditWindow
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
import app.ui


class UserPack(ObjectPack):

    model = User

    add_window = edit_window = app.ui.AllModelEditWindow.edit(model)

    add_to_desktop = True


class ContentTypePack(ObjectPack):

    model = ContentType

    observer = Observer()

    add_window = edit_window = ModelEditWindow.fabricate(
        model = model,
        field_list=['code', 'app_label'],
        model_register=observer,
    )

    add_to_desktop = True


class GroupPack(ObjectPack):
    observer = Observer()
    model = Group

    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        field_list=['code', 'name', 'permissions'],
        model_register=observer,
    )

    add_to_desktop = True


class PermissionPack(ObjectPack):
    observer = Observer()
    model = Permission

    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        field_list=['code', 'name'],
        model_register=observer,
    )
    add_to_desktop = True
