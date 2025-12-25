def print_info( a , b = [] ):
    print(b)
    return b

result = print_info(1)

result.append('error')

print_info(2)

def print_info_2( a , b = None ):
    print(b)
    return b

result = print_info_2(1)

#result.append('error')

print_info_2(2)

def print_user_info( name , *, age  , sex = '男' ):
    # 打印用户信息
    print('昵称：{}'.format(name) , end = ' ')
    print('年龄：{}'.format(age) , end = ' ')
    print('性别：{}'.format(sex))
    return;

# 调用 print_user_info 函数
print_user_info( name = '两点水' ,age = 18 , sex = '女' )

# 这种写法会报错，因为 age ，sex 这两个参数强制使用关键字参数
print_user_info( '两点水' , 18 , '女' )
#print_user_info('两点水',age='22',sex='男')