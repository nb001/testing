# 初次格式化数据库表，出现：

ValueError: Related model 'users.UserProfile' cannot be resolved


# 解决办法：

　　1.python manage.py makemigrations --empty users
　　2.python manage.py makemigrations
　　3.python manage.py migrate users
　　4.python manage.py migrate