"""empty message

Revision ID: e64da0c18a13
Revises: f3c4f7797f1a
Create Date: 2023-10-31 18:01:20.966613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e64da0c18a13'
down_revision = 'f3c4f7797f1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('guitars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('merchant_id', sa.Integer(), nullable=True),
    sa.Column('make', sa.String(length=50), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('guitar_type', sa.String(), nullable=False),
    sa.Column('body_type', sa.String(), nullable=False),
    sa.Column('wood_type', sa.String(), nullable=False),
    sa.Column('color', sa.String(), nullable=False),
    sa.Column('pickup_type', sa.String(), nullable=False),
    sa.Column('joint_type', sa.String(), nullable=False),
    sa.Column('fretboard_material', sa.String(), nullable=False),
    sa.Column('frets', sa.Integer(), nullable=False),
    sa.Column('inlays', sa.String(), nullable=False),
    sa.Column('handedness', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=False),
    sa.Column('pickguard', sa.Boolean(), nullable=True),
    sa.Column('pickup_selector', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['merchant_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopping_carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('guitarId', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['shopping_carts.id'], ),
    sa.ForeignKeyConstraint(['guitarId'], ['guitars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guitar_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('guitar_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['guitar_id'], ['guitars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guitar_images')
    op.drop_table('cart_items')
    op.drop_table('shopping_carts')
    op.drop_table('guitars')
    op.drop_table('users')
    # ### end Alembic commands ###