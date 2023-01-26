import re
#
# regexp = re.compile(r"\d{4}")
#
# m = regexp.match("12345")
# print("12345", m)
#
# # Аналогичный способ написания без использования "compile"
# m = re.match(r"\d{4}", "12345")
# print("12345", m)


# regexp = re.compile(r"^pin: (\d{4})$")
# m = regexp.match("pin: 5678")
#
# print("pin 5678", m)
# print("group(0)= ", m.group(0))
# print("group(1)= ", m.group(1))



		# ФЛАГИ КОМПИЛЯЦИИ

# compiled_regexp = re.compile(r"[a-z]*")
# m = compiled_regexp.match("asdfGHJ")
# print(m, m.group(0))
#
# compiled_regexp = re.compile(r"[a-z]*", re.IGNORECASE)		# из [a-z] в [a-zA-Z]
# m = compiled_regexp.match("asdfGHJ")
# print(m, m.group(0))


# compiled_regexp = re.compile(r".*")
# m = compiled_regexp.match("asdf\nfGHJ")
# print(m, m.group(0))
#
# compiled_regexp = re.compile(r".*", re.DOTALL)		# Перенос "\n" посчитан и выполнен
# m = compiled_regexp.match("asdf\nfGHJ")
# print(m, m.group(0))
#
# comp_regexp = re.compile(r".*", re.IGNORECASE | re.DOTALL)
# m = comp_regexp.match("qwer\nfasdfsd")
# print(m, m.group(0))



		# ПОИСК ПО ТЕКСТУ

regexp = r"((\d{1,3}\.){3}\d{1,3})"
# regexp = r"(\d{1,3}\.?){4}"
#
# text = """
# # 93.114.45.13 - - [17/May/2015:10:05:21 +0000] "GET /images/web/2009/banner.png HTTP/1.1" 200 52315 "http://www.semicomplete.com/style2.css" "Mozilla/5.0 (X11; Linux x86_64; rv:25.0) Gecko/20100101 Firefox/25.0"
# # 66.249.73.135 - - [17/May/2015:10:05:40 +0000] "GET /blog/tags/ipv6 HTTP/1.1" 200 12251 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
# # 50.16.19.13 - - [17/May/2015:10:05:10 +0000] "GET /blog/tags/puppet?flav=rss20 HTTP/1.1" 200 14872 "http://www.semicomplete.com/blog/tags/puppet?flav=rss20" "Tiny Tiny RSS/1.11 (http://tt-rss.org/)"
# # 66.249.73.185 - - [17/May/2015:10:05:37 +0000] "GET / HTTP/1.1" 200 37932 "-" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
# # """
# #
# r1 = re.compile(regexp)
# m = r1.findall(text)
# print(m)
# print(r1.findall(text))
# print(re.findall(regexp, text))



		# ЗАМЕНА ЧАСТИ СТРОКИ

# res = re.sub(regexp, "--hidden-ip--", text)
# print(res)


# def replace_func(matchobj):
# 	print(matchobj)
# 	if matchobj.group(0) == '66.249.73.135':
# 		return matchobj.group(0)
# 	else:
# 		return "--hidden-ip--"
#
#
# res = re.sub(regexp, replace_func, text)
# print(res)


# text_ = """
# 123.123.123.123.
# """

# regexp_ = r"(\d{1,3}\.?){4}"
# r2 = re.compile(regexp_)
# m2 = r2.match("1.1.1.1..fsdfasasdfsfasdf")
# print("123.123.123.123", m2)
