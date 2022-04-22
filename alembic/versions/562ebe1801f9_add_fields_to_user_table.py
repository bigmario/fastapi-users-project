"""add-fields-to-user-table

Revision ID: 562ebe1801f9
Revises: 5c53254e7b7d
Create Date: 2022-04-22 09:59:55.498573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "562ebe1801f9"
down_revision = "5c53254e7b7d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("user", sa.Column("birth_date", sa.Date()))
    op.add_column("user", sa.Column("role", sa.String()))
    op.add_column("user", sa.Column("phone", sa.String()))
    op.add_column("user", sa.Column("address", sa.String()))


def downgrade():
    op.drop_column("user", "birth_date")
    op.drop_column("user", "role")
    op.drop_column("user", "phone")
    op.drop_column("user", "address")
