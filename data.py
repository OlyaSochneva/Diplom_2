class URL:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTRATION = BASE_URL + '/api/auth/register'  # регистрация
    LOGIN = BASE_URL + '/api/auth/login'  # логин
    USER = BASE_URL + '/api/auth/user'  # получить/изменить/удалить пользователя
    ORDERS = BASE_URL + '/api/orders'  # создать заказ, получить заказы пользователя
    INGREDIENTS = BASE_URL + '/api/ingredients'  # список всех ингредиентов


class ErrorSample:
    REG_MISS_REQUIRED_FIELDS = "Email, password and name are required fields"
    REG_USER_ALREADY_EXISTS = "User already exists"
    LOGIN_INVALID_FIELDS = "email or password are incorrect"
    UNAUTHORIZED_USER = "You should be authorised"
    NO_INGREDIENTS = "Ingredient ids must be provided"


class ResponseSample:
    USER_CREATED_OR_LOGIN_SUCCESS = {
        "success": "true",
        "user": {
            "email": "",
            "name": ""
        },
        "accessToken": "",
        "refreshToken": ""
    }
    USER_INFO = {
            "success": "true",
            "user": {
                "email": "",
                "name": ""
            }
        }
    USER_ORDERS_LIST = {
        "success": "true",
        "orders": "",
        "total": "",
        "totalToday": ""
    }
    ORDER = {
        "ingredients": [],
        "_id": "",
        "status": "",
        "number": "",
        "createdAt": "",
        "updatedAt": ""
    }
    ORDER_CREATION = {
        "name": "",
        "order": {
            "number": ""
        },
        "success": "true"
    }

