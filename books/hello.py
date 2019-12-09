import graphene
from rx import Observable

class HelloSubscription(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(root, info):
        return Observable.interval(3000) \
                         .map(lambda: "hello world!")