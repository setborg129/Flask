from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: 'Aliotor',
    2: 'Mark',
    3: 'Sebastian',
    4: 'Hylion Englesio',
}


@user.route('/')
def user_list():
    return render_template(
        'users/users_list.html',
        users=USERS,
    )


@user.route('/<int:pk>')
def get_user_id(pk: int):
    "Если нет юзера по айди, то выводим изключение"
    try:
        user_name = USERS[pk]
    except KeyError:
        return f"Нет такого юзера с Id - {pk}"
    return render_template(
        'users/details.html',
        user_name=user_name,
    )
