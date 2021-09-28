"""empty message

Revision ID: cc980ab598fe
Revises: 
Create Date: 2021-09-28 09:44:50.099118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cc980ab598fe"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "github_users_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("repository", sa.String(length=70), nullable=False),
        sa.Column("languages", sa.JSON(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("stars", sa.Integer(), nullable=False),
        sa.Column("number_of_repositories", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=250), nullable=False),
        sa.Column("email", sa.String(length=250), nullable=False),
        sa.Column("password", sa.String(length=250), nullable=False),
        sa.Column("creation_date", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    op.drop_table("github_users_info")
    # ### end Alembic commands ###
