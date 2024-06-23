import factory

from app.models.product import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('name')
    display_name = factory.Faker('user_name')
    description = factory.Sequence(lambda n: f'Description Test justification {n}')
    value = factory.Faker('random_float', left_digits=None, right_digits=None, positive=False)
    available = factory.Iterator(['true', 'false', 'true'])
    audit_user_ip = factory.Faker('ipv4')
    audit_user_login = factory.Faker('user_name')
