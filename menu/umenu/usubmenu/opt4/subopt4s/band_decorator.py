class EnergyRangeError(Exception):
    def __init__(self, message:str):
        self.message = message


class EnergyRangeFormatError(Exception):
    def __init__(self, message:str):
        self.message = message


def band_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except EnergyRangeError as e:
            print_error(information="输入的能量超出范围!")
        except EnergyRangeFormatError as e:
            print_error(information="输入能量范围的格式错误!")
        except Exception as e:
            print(e)
    return wrapper


def print_error(information:str):
    '''
    Description
    -----------
        1. 当触发 `dos_decorator` 的错误后，此函数负责输出对应的信息
    '''
    print("\033[0;31m+{0:-^60}+\033[0m".format(" Error "))
    print("\033[0;31m\t* {0}\033[0m".format(information))
    print("\033[0;31m+{0:-^60}+\033[0m".format(""))