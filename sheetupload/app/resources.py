from import_export import resources
from .models import Person


class PersonsResource(resources.ModelResource):
    class Meta:
        model = Person