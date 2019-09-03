"""
A closure simply causes the inner function to remember the state
of its environment when called. Beginners often think that a
closure is the inner function, but it’s really caused by the inner
function. The closure “closes” the local variable on the stack, and
this stays around after the stack creation has finished executing .
"""

def has_permission(page):
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)
    return inner


current_user = has_permission('Admin Area')


random_user = has_permission('Admin Area')

print(current_user('Admin'))
print(random_user('Not Admin'))

# 'Admin' does have access to Admin Area.
# 'Not Admin' does NOT have access to Admin Area.