"""
create_measurements_table

Revision ID: 56e606a706e1
Revises: e62a2de1f140
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

revision = '56e606a706e1'
down_revision = 'e62a2de1f140'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('measurements',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('device_id', sa.Integer(), nullable=False),
        sa.Column('variable_id', sa.String(length=255), nullable=False),
        sa.Column('value', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('request_payload', sa.Text(), nullable=False),
        
        sa.ForeignKeyConstraint(['device_id'], ['devices.id']),
        sa.ForeignKeyConstraint(['variable_id'], ['variables.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
   op.drop_table('measurements')