#正常场景 测试数据
success_data = {"username":"hplich","password":"yHQWPdA4kBw%f0"}

# 异常用例 -手机号码格式不对(大于位、小于11位、为空、不在号码段)
phone_data = [
    {"username":"asda","password":"yHQWPdA4kBw%f0","check":"用户名或密码错误，请重新登陆！"},
    {"username": "asdasd", "password": "yHQWPdA4kBw%f0", "check": "用户名或密码错误，请重新登陆！"},
    # {"username": "", "password":"yHQWPdA4kBw%f0", "check":  "请输入域帐号/邮箱"},
    {"username": "asdasd1", "password": "yHQWPdA4kBw%f0", "check": "用户名或密码错误，请重新登陆！"}
]

# 异常用例
# class="help-block"