from objectpack.ui import BaseEditWindow, make_combo_box, ModelEditWindow, model_fields_to_controls, anchor100, \
    GenerationError, _create_control_for_field
from m3_ext.ui import all_components as ext
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User

# from app.models import User


class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__surname = ext.ExtStringField(
            label=u'Фамилия',
            name='surname',
            allow_blank=False,
            anchor='100%')

        self.field__gender = make_combo_box(
            label=u'Пол',
            name='gender',
            allow_blank=False,
            anchor='100%',
            data=User.GENDERS)

        self.field__birthday = ext.ExtDateField(
            label=u'Дата рождения',
            name='birthday',
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__surname,
            self.field__gender,
            self.field__birthday,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class ContentTypeAddWindow(BaseEditWindow):

    def _init_components(self):
        super(ContentTypeAddWindow, self)._init_components()

        self.field__content_type = ext.ExtStringField(
            label=u'content-type',
            name='content-type',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(ContentTypeAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__content_type,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(ContentTypeAddWindow, self).set_params(params)
        self.height = 'auto'


class GroupAddWindow(BaseEditWindow):

    def _init_components(self):
        super(GroupAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'group',
            name='group',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(GroupAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(GroupAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type = ext.ExtStringField(
            label=u'content_type',
            name='content_type',
            allow_blank=False,
            anchor='100%')

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'


class AllModelEditWindow(ModelEditWindow):

    def _init_components(self):
        super(ModelEditWindow, self)._init_components()
        self._controls = model_fields_to_controls(
            self.model, self, **(self.field_fabric_params or {}))

    def _do_layout(self):
        super(ModelEditWindow, self)._do_layout()

        # автоматически вычисляемая высота окна
        self.height = None
        self.layout = 'form'
        self.layout_config = {'autoHeight': True}
        self.form.layout_config = {'autoHeight': True}

        # все поля добавляются на форму растянутыми по ширине
        self.form.items.extend(list(map(anchor100, self._controls)))

    def set_params(self, params):
        super(ModelEditWindow, self).set_params(params)
        # если сгенерировано хотя бы одно поле загрузки файлов,
        # окно получает флаг разрешения загрузки файлов
        self.form.file_upload = any(
            isinstance(x, ext.ExtFileUploadField)
            for x in self._controls)

    @classmethod
    def edit(cls, model, **kwargs):
        return type('%sEditWindow' % model.__name__, (cls,), {
            'model': model, 'field_fabric_params': kwargs})
