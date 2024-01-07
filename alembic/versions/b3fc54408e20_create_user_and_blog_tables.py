"""create user and blog tables

Revision ID: b3fc54408e20
Revises:
Create Date: 2024-01-07 11:10:15.189108

"""
from typing import Sequence, Union

import sqlalchemy as sa  # noqa: F401

from alembic import op  # noqa: F401

# revision identifiers, used by Alembic.
revision: str = "b3fc54408e20"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
