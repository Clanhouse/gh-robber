"""user and github user

Revision ID: 77a87b04c82c
Revises: 
Create Date: 2021-06-02 07:22:56.151842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "77a87b04c82c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "github_users",
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("repositories_count", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("username"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=256), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("github_users")
    # ### end Alembic commands ###
