import graphene
from graphene_django.types import DjangoObjectType
from ingredientes.models import Category, Ingredient


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class Persona(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()
    
    def resolve_first_name(self, info, **kwargs):
        return "John Mario"
    
    def resolver_last_name(self, info, **kwargs):
        return "Getial Bolaños"

    def resolve_full_name(self, info, **kwargs):
        return "John Mario Getial Bolaños"

class Vocabulario(graphene.ObjectType):
    a = graphene.String()
    e = graphene.String()
    i = graphene.String()
    o = graphene.String()
    u = graphene.String()

    def resolve_a(self, info, **kwargs):
        print(type(self))
        return self[0]
    
    def resolve_e(self, info, **kwargs):
        return self[1]
    
    def resolve_i(self, info, **kwargs):
        return self[2]
    
    def resolve_o(self, info, **kwargs):
        return self[3]
    
    def resolve_u(self, info, **kwargs):
        return self[4]

class Query(object):
    reverse = graphene.String(word=graphene.String())

    persona = graphene.Field(Persona)

    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())

    all_categories = graphene.List(CategoryType)

    ingredient = graphene.Field(IngredientType,
                                id=graphene.Int(),
                                name=graphene.String())

    all_ingredients = graphene.List(IngredientType, name=graphene.String())

    vocabulario = graphene.Field(Vocabulario)

    def resolve_persona(self, info, **kwargs):
        return Persona()

    def resolve_reverse(self, info, word):
        return word[::-1]

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)
        return None

    def resolve_vocabulario(self, info, **kwargs):
        return "aeiou"
