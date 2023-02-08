from django.db import transaction
from django.shortcuts import render, redirect

from json_file_parser.forms import UploadFileJsonForms
from json_file_parser.models import FileJson


def get_form(request):
    """API для рендеринга формы"""
    form = UploadFileJsonForms()
    return render(request, 'json_file_form.html', {'form': form})


def post_form(request):
    """API для записи json в bd"""
    form = UploadFileJsonForms(request.POST, request.FILES)

    if form.is_valid():
        with transaction.atomic():
            for i in form.cleaned_data['_json_file_data']:
                FileJson.objects.create(
                    name=i['name'],
                    date=i['date']
                )

        return redirect('get_data')
    return render(request, 'json_file_form.html', {'form': form})


def get_data(request):
    """API для отображения всех записей из базы"""
    data = FileJson.objects.all()
    return render(request, 'display_data.html', {'data': data})
