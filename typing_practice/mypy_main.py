# def foo(var: int):
#     print(type(var))
#
#
# foo("bar")


def foo(var: str):
    return "foo" + str(var)


print(foo("1"))

# Чтобы запустить проверку типизации,
# сначала надо в терминале запустить: "mypy typing_practice\mypy_main.py" как пример