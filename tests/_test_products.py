
from app.models.product import Product
from tests.factory.product_factory import ProductFactory


def test_estrutura_do_banco_creat_product(session):
    new_product = Product(
        name = 'name',
        display_name='display_name',
        description='description',
        value=10,
        available='true',
        audit_user_ip='17.07.171',
        audit_user_login='login',

    )
    session.add(new_product)
    session.commit()
    produto = (
        session.query(Product)
        .filter(Product.name == 'name')
        .first()
    )
    assert produto.description == 'description'
    assert produto.name == 'name'
    assert produto.available == 'true'



def test_get_product(session, user_10):
    Product = ProductFactory.build()
    new_Product = Product(
        name = 'name',
        display_name='display_name',
        description='description',
        value=10,
        available='true',
        audit_user_ip='17.07.171',
        audit_user_login='login'
    )
    session.add(new_Product)
    session.commit()
    product = (
        session.query(Product)
        .filter(Product.name == 'name')
        .first()
    )
    assert product.value == 10
    product = (
        session.query(product)
        .filter(Product.available == 'true')
        .first()
    )
    assert product.value == 10
