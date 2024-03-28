"""Initial migration.

<<<<<<<< HEAD:server/migrations/versions/80ca967fff04_initial_migration.py
Revision ID: 80ca967fff04
Revises: 
Create Date: 2024-03-28 21:53:12.376328
========
Revision ID: 070a651509ee
Revises: 
Create Date: 2023-11-09 23:59:24.070133
>>>>>>>> origin/main:server/migrations/versions/070a651509ee_initial.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:server/migrations/versions/80ca967fff04_initial_migration.py
revision = '80ca967fff04'
========
revision = '070a651509ee'
>>>>>>>> origin/main:server/migrations/versions/070a651509ee_initial.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('mobile', sa.Integer(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('dateOfBirth', sa.Date(), nullable=True),
    sa.Column('profileUrl', sa.String(length=120), nullable=True),
    sa.Column('isAdmin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('order_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.JSON(), nullable=False),
    sa.Column('order', sa.JSON(), nullable=False),
    sa.Column('payment', sa.JSON(), nullable=False),
    sa.Column('payment_id', sa.String(length=80), nullable=True),
    sa.Column('paymenttype', sa.String(length=80), nullable=True),
    sa.Column('billerName', sa.String(length=80), nullable=True),
    sa.Column('billerId', sa.String(length=80), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=80), nullable=False),
    sa.Column('category', sa.String(length=80), nullable=False),
    sa.Column('product', sa.String(length=80), nullable=False),
    sa.Column('rate', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('sold', sa.Integer(), nullable=True),
    sa.Column('productImage', sa.String(length=120), nullable=False),
    sa.Column('availableInStock', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand_details.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_details')
    op.drop_table('order_details')
    op.drop_table('user_details')
    op.drop_table('category_details')
    op.drop_table('brand_details')
    # ### end Alembic commands ###
