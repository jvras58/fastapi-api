from app.models.product import Product


def test_estrutura_do_banco_creat_product(session):
    """
    Teste de criação de produto no banco de dados.

    Args:
        session (Session): Instancia de Session do SQLAlchemy provisionada pelo Fixture.
    """
    # GIVEN ------
    # Dada uma Instancia de produto com os dados abaixo é salva no banco de dados;
    new_product = Product(
        name='name',
        display_name='display_name',
        description='description',
        value=10,
        available=True,
        audit_user_ip='17.07.171',
        audit_user_login='login',
    )
    session.add(new_product)
    session.commit()
    # WHEN ------
    # Quando executa-se uma busca com um filtro que aponta para o produto anteriormente
    # salvo;
    produto = session.query(Product).filter(Product.name == 'name').first()
    # THEN ------
    # Então uma instancia de produto é retornada do banco de dados com os mesmos dados que
    # foi salvo anteriormente.
    assert produto.description == 'description'
    assert produto.name == 'name'
    assert produto.available is True


def test_get_product_by_id(client, token, product_10):
    """
    Testa se é possível obter um produto apartir do id.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
        product_10: produto criado para os testes.

    """
    response = client.get('/products/2', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert 'Product Test 2' in response.json()['name']
    assert 'Description Test justification' in response.json()['description']


def test_read_product(client, token, product_10):
    """
    Testa se é possível obter uma lista de produtos.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
        product_10: produto criado para os testes.

    """
    response = client.get('/products/', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert len(response.json()['Product']) > 0


def test_read_product_by_filter(client, product_10, token):
    """
    Testa se é possível obter uma lista de produtos filtrados.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        product_10: produto criado para os testes.
        token: token de autenticação.

    """
    response = client.get(
        '/products/?name=Product', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    assert len(response.json()['Product']) > 0


def test_create_product(client, token):
    """
    Testa se é possível criar um produto.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
    """
    response = client.post(
        '/products/',
        json={
            'name': 'Product Test',
            'display_name': 'Product Test',
            'description': 'Product Test Description',
            'value': 10.0,
            'available': True,
        },
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 201
    assert response.json()['name'] == 'Product Test'
    assert response.json()['description'] == 'Product Test Description'
    assert response.json()['value'] == 10.0


def test_create_product_not_found(client, token):
    """
    Testa se é possível criar um produto com os campos vazios.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
    """
    response = client.post(
        '/products/',
        json={},
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 422
    assert 'detail' in response.json()


def test_update_product(client, token, product):
    """
    Testa se é possível atualizar um produto pelo ID.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
        product: produto criado para os testes.
    """
    response = client.put(
        '/products/1',
        json={
            'name': 'Product Test Update',
            'display_name': 'Product Test Update',
            'description': 'Product Test Description Update',
            'value': 10.0,
            'available': True,
        },
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'Product Test Update'
    assert response.json()['description'] == 'Product Test Description Update'
    assert response.json()['value'] == 10.0
    assert response.json()['available'] is True


def test_update_product_not_found(client, token):
    """
    Testa se é possível atualizar um produto pelo ID inexistente.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
    """
    response = client.put(
        '/products/1',
        json={
            'name': 'Product Test Update',
            'display_name': 'Product Test Update',
            'description': 'Product Test Description Update',
            'value': 10.0,
            'available': True,
        },
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 404
    assert 'detail' in response.json()


def test_delete_product(client, token, product):
    """
    Testa se é possível deletar um produto pelo ID.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
        product: produto criado para os testes.
    """
    response = client.delete(
        '/products/1', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    assert response.json()['detail'] == 'product deleted successfully'


def test_delete_product_not_found(client, token):
    """
    Testa se é possível deletar um produto pelo ID inexistente.

    Args:
        client: objeto cliente do test_client(FASTAPI).
        token: token de autenticação.
    """
    response = client.delete(
        '/products/1', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 404
    assert 'detail' in response.json()
