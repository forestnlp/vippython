src = open('logo.png', 'rb')
target = open('logo2.png', 'wb')# r w a b(二进制）
target.write(src.read())
target.close()
src.close()
