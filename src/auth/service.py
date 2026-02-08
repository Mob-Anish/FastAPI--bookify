from .models import User
from .schemas import UserCreateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import Select
from .utils import create_hash_password


class UserService:
    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email)

        return True if user is not None else False

    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = Select(User).where(User.email == email)

        result = await session.exec(statement)

        user = result.first()

        return user

    async def create_user(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        new_user.password_hash = create_hash_password(
            user_data_dict["password"])

        session.add(new_user)
        await session.commit()

        return new_user
