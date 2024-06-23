import random

import factory

from app.models.product import Product


class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f'Product Test {n}')
    display_name = factory.Faker('user_name')
    description = factory.Sequence(lambda n: f'Description Test justification {n}')
    value = factory.LazyFunction(
        lambda: round(random.uniform(1.0, 100.0), 2)
    )  # Gera um float aleatório entre 1.0 e 100.0  # noqa: E501
    available = factory.Iterator([True, False, True])
    audit_user_ip = factory.Faker('ipv4')
    audit_user_login = factory.Faker('user_name')
    audit_user_ip = factory.Faker('ipv4')
    audit_user_login = factory.Faker('user_name')
