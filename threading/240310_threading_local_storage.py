# Напишите функцию логирования print_msg, которая подготавливает и выводит сообщение о работе потока по шаблону:
# <Сообщение>, fileno=<файловый дескриптор>, <право доступа>
# где: <Сообщение> - атрибут msg локального хранилища потока;
# <файловый дескриптор> - файловый дескриптор, атрибут fileno хранилища, целое число;
# <право доступа> - доступ к файлу, атрибут permission, строка.

# Например:
# deleted ID 4660, fileno=11128, DOMAIN\admin

# При этом, если атрибут permission не установлен, в правах доступа следует выводить guest
# Если атрибуты msg или fileno не установлены, вместо них следует выводить failure

# Например, предыдущая запись без атрибута msg и permission:
# failure, fileno=11128, guest



from threading import local

stor_local = local()


def print_msg(stor_local: local) -> None:
    msg = getattr(stor_local, 'msg', 'failure')
    fileno = getattr(stor_local, 'fileno', 'failure')
    permission = getattr(stor_local, 'permission', 'guest')
    print(f'{msg}, fileno={fileno}, {permission}')