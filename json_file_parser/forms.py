import datetime
import json

from django import forms


class UploadFileJsonForms(forms.Form):
    """Форма для загрузки файла .json"""
    json_file = forms.FileField(label="Выбери JSON файл для загрузки",
                                required=True,
                                error_messages={
                                    "required": "Прикрепите файл!"
                                })

    # валидация
    def clean_json_file(self):
        json_file = self.cleaned_data['json_file']

        if not json_file.name.endswith(".json"):
            self.add_error('json_file', 'Файл не JSON формата.')
            return

        try:
            json_data = json.load(self.cleaned_data['json_file'])
        except json.decoder.JSONDecodeError:
            self.add_error('json_file', 'Не возможно прочитать JSON.')
            return

        if not isinstance(json_data, list):
            self.add_error('json_file', 'Невалидные данные в файле')
            return

        for i in json_data:
            if 'name' not in i and 'date' not in i:
                self.add_error('json_file', 'JSON содержит невалидные ключи.')
                return

            if len(i['name']) >= 50:
                self.add_error('json_file', 'Значение ключа "name" в JSON содержит более 50 символов.')
                return

            try:
                i['date'] = datetime.datetime.strptime(i['date'], "%Y-%m-%d_%H:%M")
            except ValueError:
                self.add_error('json_file', 'JSON содержит неправильный формат даты и времени.')
                return

        self.cleaned_data['_json_file_data'] = json_data
        return self.cleaned_data['json_file']
