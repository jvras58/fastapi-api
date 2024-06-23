from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi import status as HTTP_STATUS
from sqlalchemy.orm import Session

from app.api.authentication.controller import get_current_user
from app.api.products.schemas import ProductListSchema, ProductPublic, ProductSchema
from app.database.session import get_session
from app.models.product import Product
from app.models.user import User
from app.utils.base_schemas import SimpleMessageSchema
from app.utils.exceptions import ObjectConflitException, ObjectNotFoundException
from app.utils.generic_controller import GenericController

router = APIRouter()

Product_controller = GenericController(Product)

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.get(
    '/{product_id}',
    status_code=HTTP_STATUS.HTTP_200_OK,
    response_model=ProductPublic,
)
def get_product_by_id(product_id: int, db_session: Session, current_user: CurrentUser):
    return Product_controller.get(db_session, product_id)


@router.get('/', status_code=HTTP_STATUS.HTTP_200_OK, response_model=ProductListSchema)
def get_all_product(
    db_session: Session,
    current_user: CurrentUser,
    skip: int = 0,
    limit: int = 100,
    name: str = None,
    value: float = None,
):

    criterias = {}
    if name:
        criterias['name'] = name
    if value:
        criterias['value'] = value

    products: list[Product] = Product_controller.get_all(
        db_session, skip, limit, **criterias
    )
    return {'Product': products}


@router.post(
    '/', status_code=HTTP_STATUS.HTTP_201_CREATED, response_model=ProductSchema
)
def create_new_product(
    product: ProductSchema,
    request: Request,
    db_session: Session,
    current_user: CurrentUser,
):
    new_product_instance = Product(**product.model_dump())
    new_product_instance.audit_user_login = current_user.username
    new_product_instance.audit_user_ip = request.client.host
    try:
        return Product_controller.save(db_session, new_product_instance)
    except ObjectConflitException as ex:
        raise HTTPException(status_code=409, detail=ex.args[0]) from ex
    except ObjectNotFoundException as ex:
        raise HTTPException(status_code=404, detail=ex.args[0]) from ex


@router.put(
    '/{product_id}',
    status_code=HTTP_STATUS.HTTP_200_OK,
    response_model=ProductSchema,
)
def update_product(
    product_id: int,
    product: ProductSchema,
    request: Request,
    db_session: Session,
    current_user: CurrentUser,
):
    product_instance_update = Product(**product.model_dump())
    product_instance_update.id = product_id
    product_instance_update.audit_user_login = current_user.username
    product_instance_update.audit_user_ip = request.client.host
    try:
        return Product_controller.update(db_session, product_instance_update)
    except ObjectNotFoundException as ex:
        raise HTTPException(status_code=404, detail=ex.args[0]) from ex


@router.delete(
    '/{product_id}',
    status_code=HTTP_STATUS.HTTP_200_OK,
    response_model=SimpleMessageSchema,
)
def delete_product(
    product_id: int,
    db_session: Session,
    current_user: CurrentUser,
):
    try:
        Product_controller.delete(db_session, product_id)
    except ObjectNotFoundException as ex:
        raise HTTPException(status_code=404, detail=ex.args[0]) from ex
    return {'detail': 'product deleted successfully'}
