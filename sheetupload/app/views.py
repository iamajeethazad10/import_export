from django.shortcuts import render
from . models import Person
from .resources import PersonsResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


def export(request):
    person_resource = PersonsResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response


def simple_upload(request):
    if request.method == 'POST':
        persons_resource = PersonsResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        if not new_persons.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_persons.read(), format='xlsx')
        for data in imported_data:
            value = Person(
                data[0],
                data[1],
                data[2],
                data[3],
                )
            value.save()
    return render(request, 'upload.html')