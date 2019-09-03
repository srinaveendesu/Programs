import functools

user = {'username': 'jose123', 'access_level': 'user'}

# notice the three functions defined one within another
def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return my_decorator


@user_has_permission('user')
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel.
    """
    return f'Password for {panel} panel is 1234.'


print(my_function.__name__)
print(my_function('movies'))

# Decorator unwrapping happens in the following way
user_has_p = user_has_permission('user')
my_func = user_has_p(my_function)
print (my_func('games'))

# my_function
# Password for movies panel is 1234.
# Password for games panel is 1234.