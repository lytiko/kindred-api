from datetime import datetime
import pytz
import graphene
from graphene.types import Scalar

class Query(graphene.ObjectType):
    """The root query object. It supplies the user attribute, which is the
    portal through which other attributes are accessed."""

    user = graphene.Field("core.queries.UserType")
    

    def resolve_user(self, info, **kwargs):
        """Gets the user associated with the request, and returns that."""

        return info.context.user


schema = graphene.Schema(query=Query)