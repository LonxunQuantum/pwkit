def print_error(information:str):
    print("\033[0;31m+{0:-^60}+\033[0m".format(" Error "))
    print("\033[0;31m\t* {0}\033[0m".format(information))
    print("\033[0;31m+{0:-^60}+\033[0m".format(""))


def dos_decorator(func):
    '''
    Parameters
    ----------  
        1. func: 函数
    '''
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as ke:  # 输入的能量范围过大
            print_error(information="输入的能量超出范围!")
        except IndexError as ie:    # 仅输入了 1
            print_error(information="输入能量范围的格式错误!")
        except ValueError as ve:    # -2,,2
            print_error(information="输入能量范围的格式错误!")
    return wrapper

