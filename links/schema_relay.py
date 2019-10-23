import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from links.models import Link, Vote


class LinkFilter(django_filters.FilterSet):
    url = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    """
    #1 Relay allows you to use django-filter for filtering data.
     Here, you’ve defined a FilterSet, with the url and description fields.
    """
    class Meta:
        model = Link
        fields = ['url', 'description']


class LinkNode(DjangoObjectType):
    """
    #2: The data is exposed in Nodes, so you must create one for the links.
    """
    class Meta:
        model = Link
        # 3: Each node implements an interface with an unique ID (you’ll see the result of this in a bit).
        interfaces = (graphene.relay.Node,)


class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node, )


class RelayQuery(graphene.ObjectType):
    # 4: Uses the LinkNode with the relay_link field inside your new query.
    relay_link = graphene.relay.Node.Field(LinkNode)
    # 5: Defines the relay_links field as a Connection, which implements the pagination structure.
    relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)


class RelayCreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String(required=True)
        description = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user or None

        link = Link(
            url=input.get('url'),
            description=input.get('description'),
            posted_by=user,
        )
        link.save()

        return RelayCreateLink(link=link)


class RelayMutation(graphene.AbstractType):
    relay_create_link = RelayCreateLink.Field()

# class RelayCreateLink(graphene.relay.ClientIDMutation):
#     link = graphene.Field(LinkNode)
#
#     class Input:
#         url = graphene.String()
#         description = graphene.String()
#
#     #def mutate(root, info, **input):
#     def mutate_and_get_payload(root, info, **input):
#         user = info.context.user or None
#
#         link = Link(
#             url=input.get('url'),
#             description=input.get('description'),
#             posted_by=user,
#         )
#         link.save()
#
#         return RelayCreateLink(link=link)
#
#
# class RelayMutation(graphene.AbstractType):
#     relay_create_link = RelayCreateLink.Field()

