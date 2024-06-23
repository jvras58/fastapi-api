from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.user import user_product_association
from app.utils.base_model import AbstractBaseModel


class Product(AbstractBaseModel):
    """
    Representa a tabela Produto no banco de dados.
    """

    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    display_name: Mapped[str] = mapped_column(name='str_display_name')
    name: Mapped[str] = mapped_column(name='str_product_name')
    description: Mapped[str] = mapped_column(name='str_product_descrition')
    value: Mapped[str] = mapped_column(name='float_value_product')
    available: Mapped[bool] = mapped_column(name='bool_available_product')

    # Relacionamento com User
    users = relationship(
        'User', secondary=user_product_association, back_populates='products'
    )
