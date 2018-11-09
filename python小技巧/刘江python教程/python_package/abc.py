# 在自定义模块的时候，对模块的命名一定要注意，不要和官方标准模块以及一些比较有名的第三方模块重名，一有不慎，就容易出现模块导入错误的情况发生


def my_abs():
    print("my_abs!")


if __name__ == '__main__':
    my_abs()