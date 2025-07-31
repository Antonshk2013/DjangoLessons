from rest_framework.request import Request

from src.users.repository import UserRepository
from src.shared.base_service_response import ServiceResponse, ErrorType
from src.users.dtos import ListUsersDTO, DetailedUserDTO, ChangePasswordDTO


class UserService:
    repository = UserRepository()

    def get_all_users(self):
        try:
            data = self.repository.get_all()

            serializer = ListUsersDTO(data, many=True)

            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except Exception as e:
            return ServiceResponse(
                success=False,
                message=f"Error retrieving users: {str(e)}",
                error_type=ErrorType.UNKNOWN_ERROR
            )

    def get_user_by_id(self, user_id: int):
        try:
            user = self.repository.get_by_id(user_id)

            if user is None:
                return ServiceResponse(
                    success=False,
                    message=f"User with ID {user_id} not found",
                    error_type=ErrorType.NOT_FOUND
                )

            serializer = DetailedUserDTO(user)

            return ServiceResponse(
                success=True,
                data=serializer.data
            )
        except Exception as e:
            return ServiceResponse(
                success=False,
                message=f"Error retrieving user: {str(e)}",
                error_type=ErrorType.UNKNOWN_ERROR
            )

    def update_user_password(self, request: Request) -> ServiceResponse:
        serializer = ChangePasswordDTO(request.data)
        if not serializer.is_valid():
            return ServiceResponse(
                success=False,
                error_type=ErrorType.VALIDATION_ERROR,
                message=serializer.errors)
        user = request.user
        if not user.check_password(serializer.data['old_password']):
            return ServiceResponse(
                success=False,
                error_type=ErrorType.VALIDATION_ERROR,
                message="Неверный пароль")
        user.set_password(serializer.data['new_password'])
        user.save()
        return ServiceResponse(
            success=True,
            message="Пароль успешно изменен"
        )
