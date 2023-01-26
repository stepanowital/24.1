		# ЗАЧЕМ ИСПОЛЬЗОВАТЬ. СИНТАКСИС

from functools import wraps

# def decor(func):
# 	print("decor")
# 	@wraps(func)
# 	def wrapper(*args, **kwargs):
# 		print("wrapping")
# 		return func(*args, **kwargs)
# 	return wrapper
#
#
# @decor
# def some_func():
# 	print(some_func)
# 	pass

# some_func()


# ЧЕМУ ЭКВИВАЛЕНТНО

# def some_func2():
# 	print("some_func2")
#
#
# decor(some_func2)()


		# ДЕКОРАТОР ЗАМЕРА ВРЕМЕНИ ИСПОЛНЕНИЯ

import time
from functools import wraps


# def logtime(func):
# 	@wraps(func)
# 	def _wrapper(*args, **kwargs):
# 		t = time.time()
# 		try:
# 			return func(*args, **kwargs)
# 		finally:
# 			print("Время на выполнение программы -", time.time() - t)
#
# 	return _wrapper
#
#
# @logtime
# def consumer():
# 	for i in range(1, 6):
# 		print(i)
# 		time.sleep(1)
# 	# 1 / 0
#
#
# consumer()


		# ДЕКОРАТОР, ПРИНИМАЮЩИЙ ТАЙМАУТ, ЕСЛИ ВРЕМЯ ВЫПОЛНЕНИЯ БОЛЬШЕ - ВЫВОДИМ ДОП. СООБЩЕНИЕ

import time
from functools import wraps


def logtime_t(time_limit):
	print("logtime_t")
	def decor(func):
		print("decor")
		@wraps(func)
		def _wrapper(*args, **kwargs):
			print("_wrapper")
			t = time.time()
			try:
				return func(*args, **kwargs)
			finally:
				res = time.time() - t
				if res >= time_limit:
					print("Время на выполнение программы -", res)
		return _wrapper
	return decor


# @logtime_t(1)
def consumer():
	for i in range(50000000):
		pass


# consumer()
# decor = logtime_t(1)
# new_consumer = decor(consumer)
# new_consumer()
# или
logtime_t(1)(consumer)()
