class EnergyRangeError(Exception):
    '''
    Description
    -----------
        1. 当输入的能量区间超出能量范围，引发的异常
            e.g.
            能量范围是 -63.805 eV ~ 7.238 eV。输入绘制的能量范围 (e.g. -2,2)
            ------------>>
            -10,20
    '''
    def __init__(self, message:str):
        self.message = message


class EnergyRangeFormatError(IndexError, ValueError):
    '''
    Description
    -----------
        1. 当输入的能量区间格式错误，引发的异常 (IndexError)
            e.g.
            能量范围是 -63.805 eV ~ 7.238 eV。输入绘制的能量范围 (e.g. -2,2)
            ------------>>
            -10
        2. 当输入的能量区间格式错误，引发的异常 (ValueError)
            e.g.
            能量范围是 -63.805 eV ~ 7.238 eV。输入绘制的能量范围 (e.g. -2,2)
            ------------>>
            -10,,20
    '''
    def __init__(self, message:str):
        self.message = message


class Element2OrbitalFormatError(KeyError, IndexError):
    '''
    Description
    -----------
        1. KeyError
            e.g.
            +---------------------------- Warm Tips -----------------------------+
            * 存在的原子及轨道:
            - Mo : 4s, 4px, 4py, 4pz, 4dxy, 4dxz, 4dyz, 4dz2, 4d(x^2-y^2), 5s, 
            - S  : 3s, 3px, 3py, 3pz, 

            * 注意事项:
            - 格式: <元素>: <轨道1>, <轨道2>, ...
            - 输入“回车键”后，即可输入下一个原子以及对应轨道
            - 连续输入两次“回车键”后，开始绘制
            - 示例: Mo:4d(x^2-y^2), 4dxy, 4dz2
            +--------------------------------------------------------------------+
            输入绘制的原子(index=1)及轨道:
            ------------>>
            Mo:
            
            KeyError: "['mo-'] not in index"
        2. IndexError
            e.g.
            +---------------------------- Warm Tips -----------------------------+
            * 存在的原子及轨道:
            - Mo : 4s, 4px, 4py, 4pz, 4dxy, 4dxz, 4dyz, 4dz2, 4d(x^2-y^2), 5s, 
            - S  : 3s, 3px, 3py, 3pz, 

            * 注意事项:
            - 格式: <元素>: <轨道1>, <轨道2>, ...
            - 输入“回车键”后，即可输入下一个原子以及对应轨道
            - 连续输入两次“回车键”后，开始绘制
            - 示例: Mo:4d(x^2-y^2), 4dxy, 4dz2
            +--------------------------------------------------------------------+
            输入绘制的原子(index=1)及轨道:
            ------------>>
            Mo
            
            Out range of list
    '''
    def __init__(self, message:str):
        self.message = message


def dos_decorator(func):
    '''
    Description
    -----------
        1. 处理绘制DOS时，由于用户输入错误产生的各种异常(Exception)
    
    Parameters
    ----------
        1. func: 函数
    '''
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except EnergyRangeError as ke:  # 输入的能量范围过大
            print_error(information="输入的能量超出范围!")
        except IndexError as ie:    # 仅输入了 1
            if isinstance(ie, EnergyRangeFormatError):
                print_error(information="输入能量范围的格式错误!")
            elif isinstance(ie, Element2OrbitalFormatError):
                print_error(information="输入原子及轨道的格式错误!")
            else:
                print(ie)
        except ValueError as ve:    # -2,,2
            if isinstance(ve, EnergyRangeFormatError):
                print_error(information="输入能量范围的格式错误!")
            else:
                print(ve)
        except KeyError as ke:
            if isinstance(ke, Element2OrbitalFormatError):
                print_error(information="输入原子及轨道的格式错误!")
            else:
                print(ke)
                
    return wrapper



def orbital_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            pass
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