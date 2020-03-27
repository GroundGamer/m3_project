from objectpack.ui import ModelEditWindow, model_fields_to_controls, anchor100
from m3_ext.ui import all_components as ext


class AllModelEditWindow(ModelEditWindow):

    def _init_components(self):
        super(ModelEditWindow, self)._init_components()
        self._controls = model_fields_to_controls(
            self.model, self)

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
    def edit(cls, model):
        return type('%sEditWindow' % model.__name__, (cls,), {
            'model': model})
