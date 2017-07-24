class User:
    """Info about users"""
    def __init__(self, f_name, l_name, age, login_attempts):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_users(self):
        print(self.l_name + " " + self.f_name + " " + str(self.age) + " years" +
              ' and number attemps = ' + str(self.login_attempts))

    def greet_users(self):
        return "Hello " + self.f_name

    def increment_login_attemps(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attemps(self):
        self.login_attempts = 0

user_1 = User('Vlad', 'Petrov', '19', 1)
user_1.increment_login_attemps()
user_1.describe_users()
user_1.reset_login_attemps()
user_1.describe_users()


class Admin(User):
    """Privileges for admin"""
    def __init__(self, f_name, l_name, age, login_attempts):
        super().__init__(f_name, l_name, age, login_attempts)
        self.privileges = ['You can add message', 'You can delete users',
                           'You can banned users']

    def show_privileges(self):
        print("Admin privileges: ")
        for i in self.privileges:
            print(i)

admin = Admin('Stive', 'Jobs', '50', 1)
admin.describe_users()
admin.show_privileges()

if __name__ == '__main__':
    main()
