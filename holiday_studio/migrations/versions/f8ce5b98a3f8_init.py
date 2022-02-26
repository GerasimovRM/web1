"""init

Revision ID: f8ce5b98a3f8
Revises: 
Create Date: 2022-02-26 11:51:54.177485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8ce5b98a3f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Order',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('describtion', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('sqlite_sequence')
    op.drop_table('order')
    op.alter_column('client', 'phone',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('client', 'email',
               existing_type=sa.TEXT(),
               nullable=True)
    op.create_unique_constraint(None, 'client', ['email'])
    op.alter_column('client_order', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('employee', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('employee_position', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employee_position', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.alter_column('employee', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.alter_column('client_order', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.drop_constraint(None, 'client', type_='unique')
    op.alter_column('client', 'email',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('client', 'phone',
               existing_type=sa.TEXT(),
               nullable=False)
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('price', sa.REAL(), nullable=False),
    sa.Column('title', sa.NUMERIC(), nullable=True),
    sa.Column('describtion', sa.NUMERIC(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    op.drop_table('Order')
    # ### end Alembic commands ###