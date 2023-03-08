import os
import sys
import joblib


def write_input_output():
    '''
    Description
    -----------
        1. 向 `etot.input` 写入 `输入输出设置`
    
    Example
    -------
    #输入输出设置
    '''
    try: 
        etot_writer_path = os.path.join(os.getcwd(), "etot_writer.pkl")
        etot_writer = joblib.load(etot_writer_path)
    except:
        print("Error!!! check your input.")
    
    
    try:    # 任务类型为 Nonscf 时，需要选择 `IN.KPT = T/F`
        in_kpt_for_ns = sys.argv[4]
    except:
        in_kpt_for_ns = False
        
    etot_writer.write_input_output(
                        pseudo_name = sys.argv[1],
                        atom_config_format_file_name = sys.argv[2],
                        pseudo_dir_path = sys.argv[3],
                        in_kpt_for_ns=in_kpt_for_ns,
                        )


if __name__ == "__main__":
    write_input_output()