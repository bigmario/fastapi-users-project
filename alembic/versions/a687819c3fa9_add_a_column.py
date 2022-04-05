"""Add a column

Revision ID: a687819c3fa9
Revises: 2a282df2337e
Create Date: 2022-04-05 14:09:08.677354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a687819c3fa9"
down_revision = "2a282df2337e"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("account", sa.Column("last_transaction_date", sa.DateTime))


def downgrade():
    op.drop_column("account", "last_transaction_date")
