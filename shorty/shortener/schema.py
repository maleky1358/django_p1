import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q
from shortener import models
from .models import URLs


#class URLType(DjangoObjectType):
#    class Meta:
#        model = URL


#class Query(graphene.ObjectType):
#    urls = graphene.List(URLType, url=graphene.String(), first=graphene.Int(), skip=graphene.Int())
#    url = models.URL.full_url
##
#        if url:
#            _filter = Q(full_url__icontains=url)
#            queryset = queryset.filter(_filter)
#
#        if first:
#            queryset = queryset[:first]

#        if skip:
#            queryset = queryset[skip:]
#
#
#        return queryset
#
#    def __str__(self):
#        return '%s, %s' % (self.url, URL.objects.all())
#
#
#class CreateURL(graphene.Mutation):
#    url = graphene.Field(URLType)

#    class Arguments:
#        full_url = graphene.String()
#
#    def mutate(self, info, full_url):
#        url = URL(full_url=full_url)
#        url.save()
#
#        return CreateURL(url=url)


#class Mutation(graphene.ObjectType):
#    create_url = CreateURL.Field()
#
#    def __str__(self):
#        return self.create_url
