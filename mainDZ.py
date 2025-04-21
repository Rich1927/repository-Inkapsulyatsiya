# Используется инкапсуляция: все атрибуты User и Admin скрыты (начинаются с __), доступ к ним возможен только через геттеры/сеттеры.
## Класс Admin наследуется от User, и имеет доступ к его методам, а также расширен дополнительной логикой (уровень доступа 'admin', методы add_user и remove_user).
## В системе можно завести не более 5 пользователей, включая администраторов.

class User:
   #Класс User Представляет обычного сотрудника. Инкапсулирует: __user_id — уникальный ID.
#__name — имя. __access_level — фиксированный уровень доступа 'user'.
#Доступ к этим полям — только через методы (get_user_id(), get_name() и т.д.).
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

   # Доступ к этим полям — только через методы (get_user_id(), get_name() и т.д.).
    # Геттеры
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    # Сеттеры (если потребуется)
    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f"ID: {self.__user_id}, Name: {self.__name}, Access: {self.__access_level}"


class Admin(User):
    # Класс Admin Наследуется от User, то есть получает всё, что есть у User.
# Добавляет атрибут __admin_access_level = 'admin'.
# Добавляет два метода: add_user(user_list, user) — добавляет нового пользователя в список.
# remove_user(user_list, user_id) — удаляет пользователя из списка по ID.
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__admin_access_level = 'admin'

    def get_admin_access_level(self):
        return self.__admin_access_level

    def add_user(self, user_list, user):
        if len(user_list) < 5:
            user_list.append(user)
            print(f"User {user.get_name()} added.")
        else:
            print("Cannot add more users. Limit reached.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"User {user.get_name()} removed.")
                return
        print("User not found.")

    def __str__(self):
        return f"ID: {self.get_user_id()}, Name: {self.get_name()}, Access: {self.__admin_access_level}"


# Пример использования
#  В main-блоке:# Создаются два администратора: admin1 и admin2.
# Создаются три обычных пользователя: user1, user2, user3.
# Эти пользователи добавляются в user_list через add_user метод админов.
# Затем программа выводит список всех пользователей в user_list.
# После этого удаляется пользователь с ID = 4 (пригожин)
# И снова печатается список оставшихся пользователей.

if __name__ == "__main__":
    user_list = []

    # Создаём администраторов
    admin1 = Admin(1, "Мутин")
    admin2 = Admin(2, "Матвиенко")
    admin1.add_user(user_list, admin1)
    admin2.add_user(user_list, admin2)

    # Добавляем обычных пользователей
    user1 = User(3, "Шойгу")
    user2 = User(4, "Пригожин")
    user3 = User(5, "Володин")

    # Добавление пользователей через администратора
    admin1.add_user(user_list, user1)
    admin1.add_user(user_list, user2)
    admin2.add_user(user_list, user3)

    # Печать списка пользователей
    print("\nCurrent users:")
    for u in user_list:
        print(u)

    # Удаление пользователя
    admin1.remove_user(user_list, 4)

    # Печать списка после удаления
    print("\nUsers after removal:")
    for u in user_list:
        print(u)
