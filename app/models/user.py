from sqlalchemy import Column, ForeignKey, Index, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base_model import AbstractBaseModel

# Definição da tabela associativa
user_product_association = Table(
    'user_product_association',
    AbstractBaseModel.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('product_id', ForeignKey('product.id'), primary_key=True),
)


class User(AbstractBaseModel):
    """
    Representa a tabela Usuário no banco de dados.
    """

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, name='id')
    display_name: Mapped[str] = mapped_column(name='str_display_name')
    username: Mapped[str] = mapped_column(name='str_username')
    password: Mapped[str] = mapped_column(name='str_password')
    email: Mapped[str] = mapped_column(name='str_email')

    # Relacionamento com Product
    products = relationship(
        'Product', secondary=user_product_association, back_populates='users'
    )

    __table_args__ = (
        Index('idx_user_username', username, unique=True),
        Index('idx_user_email', email, unique=True),
    )
