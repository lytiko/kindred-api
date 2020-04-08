import graphene
from graphene_django.types import DjangoObjectType
from graphene.relay import Connection, ConnectionField
from core.queries import get_filter_arguments, get_objects, Countable
from .models import Person

class HasPeople:
    """An object type with people."""

    person = graphene.Field(
        "people.queries.PersonType", id=graphene.String(required=True)
    )
    people = ConnectionField(
        "people.queries.PersonConnection", **get_filter_arguments(Person)
    )

    def resolve_person(self, info, **kwargs):
        try:
            return self.people.get(id=int(kwargs["id"]))
        except AttributeError: return self.iterable.people.get(id=kwargs["id"])
    

    def resolve_people(self, context, **kwargs):
        try:
            return get_objects(self.people, kwargs)
        except AttributeError: return get_objects(self.iterable.people, kwargs)

        

class PersonType(DjangoObjectType):
    """A lytiko Person."""

    class Meta:
        model = Person
        exclude_fields = []
    
    id = graphene.ID()



class PersonConnection(Countable, Connection):
    """A list of People."""

    class Meta:
        node = PersonType