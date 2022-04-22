"""add-last-name-to-user-table

Revision ID: 5c53254e7b7d
Revises: 
Create Date: 2022-04-22 08:39:39.325847

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table


# revision identifiers, used by Alembic.
revision = "5c53254e7b7d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("user", sa.Column("last_name", sa.String()))


def downgrade():
    op.drop_column("user", "last_name")
