"""
create devices table

Revision ID: 1e41e995e7c4
Revises: 
"""
from alembic import op
import sqlalchemy as sa

revision = '1e41e995e7c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('devices',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('ip', sa.String(length=255), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('devices')
