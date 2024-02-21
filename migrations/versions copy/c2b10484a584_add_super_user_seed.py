"""add super user - seed

Revision ID: c2b10484a584
Revises: 030fdfb77648
Create Date: 2023-12-11 15:34:49.921941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.models import assignment, authorization


# revision identifiers, used by Alembic.
revision: str = 'c2b10484a584'
down_revision: Union[str, None] = '030fdfb77648'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # INSER USER
    op.execute('INSERT INTO "user" (str_username, str_display_name, str_email, str_password, audit_user_ip, audit_user_login) VALUES(\'admin\', \'Administrador\', \'admin@teste.com.br\', \'$2b$12$61p1Fj9Bpsb7f/0HgeMl0Ohgjcl9X.tM3D44MIUxkVCR2W6dOmAuO\', \'0.0.0.0\', \'system\')')
    
    # INSERT ROLE
    op.execute('INSERT INTO "role" (str_name, str_description, audit_user_ip, audit_user_login) VALUES(\'SUPER ADMIN\', \'Role for system Administrator\', \'0.0.0.0\', \'system\')')

    # INSERT ASSIGNMENT
    assignment_sql = 'INSERT INTO "assignment" (role_id, user_id, audit_user_ip, audit_user_login) VALUES('
    assignment_sql += '(SELECT r.id role_id  FROM "role" r WHERE r.str_name = \'SUPER ADMIN\'),'
    assignment_sql += '(SELECT u.id user_id FROM "user" u WHERE u.str_username = \'admin\'),'
    assignment_sql += '\'0.0.0.0\', \'system\')'
    op.execute(assignment_sql)

    # INSERT AUTHORIZATION
    authorization_sql = 'INSERT  INTO  "authorization" (role_id, transaction_id, audit_user_ip, audit_user_login) '
    authorization_sql += 'SELECT role_temp.role_id ,t.id trasaction_id, \'0.0.0.0\', \'system\' FROM "transaction" t, '
    authorization_sql += '(SELECT r.id role_id FROM "role" r WHERE r.str_name = \'SUPER ADMIN\') role_temp'
    op.execute(authorization_sql)


def downgrade() -> None:
    op.execute('DELETE FROM "authorization" WHERE role_id = (SELECT r.id role_id FROM "role" r WHERE r.str_name = \'SUPER ADMIN\')')
    op.execute('DELETE FROM "assignment" WHERE role_id = (SELECT r.id role_id FROM "role" r WHERE r.str_name = \'SUPER ADMIN\')')
    op.execute('DELETE FROM "role" WHERE str_name=\'SUPER ADMIN\'')
    op.execute('DELETE FROM "user" WHERE str_username=\'admin\'')
