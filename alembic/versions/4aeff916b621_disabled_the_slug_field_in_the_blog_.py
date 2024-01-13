"""Disabled the slug field in the blog table.

Revision ID: 4aeff916b621
Revises: b3fc54408e20
Create Date: 2024-01-13 08:27:02.977672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4aeff916b621'
down_revision: Union[str, None] = 'b3fc54408e20'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
