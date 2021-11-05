from random import seed
from random import randint
from random import choice
import forgery_py
from sqlalchemy.exc import IntegrityError
from . import db
from app.models import GithubUserInfo
from app.models import GithubUserInfoSchema


LANGUAGE_LIST = [
    "JavaScript",
    "Java",
    "Python",
    "PHP",
    "C++",
    "C#",
    "TypeScript",
    "R",
    "Swift",
    "Kotlin",
    "Rust",
    "Julia",
]


def create_fake_info(count=10):
    """Create sample data to database"""
    seed()
    for _ in range(count):
        fake_info = GithubUserInfo(
            id=None,
            username=forgery_py.internet.user_name(True),
            languages=[choice(LANGUAGE_LIST)],
            date=forgery_py.date.date(),
            stars=randint(1, 100),
            number_of_repositories=randint(1, 10),
            repository=str(randint(1, 100)).join("repo")
        )
        db.session.add(fake_info)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
