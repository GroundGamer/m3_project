from objectpack.actions import ObjectPack
from objectpack.observer import Observer
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
import app.ui


class UserPack(ObjectPack):

    model = User

    add_window = app.ui.UserAddWindow

    add_window = edit_window = app.ui.AllModelEditWindow.edit(model=model)

    add_to_desktop = True


class ContentTypePack(ObjectPack):

    model = ContentType

    add_window = app.ui.ContentTypeAddWindow

    add_to_desktop = True


class GroupPack(ObjectPack):

    model = Group

    add_window = app.ui.GroupAddWindow

    add_to_desktop = True


class PermissionPack(ObjectPack):
    observer = Observer()
    model = Permission

    add_window = app.ui.PermissionAddWindow

    edit_window = app.ui.AllModelEditWindow.edit(
        model,
        field_list=['code', 'name'],
        model_register=observer,
    )
    add_to_desktop = True
