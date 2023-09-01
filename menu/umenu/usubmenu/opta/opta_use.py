import os
from typing import Dict, Union

from matersdk.io.pwmat.output.report import Report
from matersdk.io.pwmat.output.outfermi import OutFermi


def opt_a():
    ### Step 1. 检查当前目录下是否存在
    ###         1) REPORT   2) OUT.FERMI
    current_path = os.getcwd()
    report_path = os.path.join(current_path, "REPORT")
    out_fermi_path = os.path.join(current_path, "OUT.FERMI")
    report_mark = os.path.exists(report_path)
    out_fermi_mark = os.path.exists(out_fermi_path)
    
    report_object = Report(report_path=report_path)
    out_fermi_object = OutFermi(out_fermi_path=out_fermi_path)
    
    ### Case 1. REPORT 和 OUT.FERMI 都不存在
    if (not report_mark) and (not out_fermi_mark):
        print("\n\033[1;31m - Error: 当前目录下缺少 REPORT 文件和 OUT.FERMI 文件!\033[0m\n", end="")
        raise SystemExit
    
    ### Case 2. 不存在 REPORT
    if not report_mark:
        print("\n\033[1;31m - Error: 当前目录下缺少 REPORT 文件!\033[0m\n", end="")
        raise SystemExit
        
    ### Case 3. 不存在 OUT.FERMI
    if not out_fermi_mark:
        print("\n\033[1;31m - Error: 当前目录下缺少 OUT.FERMI 文件!\033[0m\n", end="")
        raise SystemExit
    
    if report_object._is_metal(out_fermi_path=out_fermi_path):
        print_sum_metal()
        raise SystemExit
    
    ### Step 2. 得到能带的类型 -- bandgap_type
    bandgap_type_ = report_object.get_bandgap_type(out_fermi_path=out_fermi_path)
    if (bandgap_type_ == 0):
        bandgap_type = "间接带隙"
    else:
        bandgap_type = "直接带隙"
    
    ### Step 3. 得到带隙的大小 -- bandgap
    bandgap = report_object.get_bandgap(out_fermi_path=out_fermi_path)
    
    ### Step 4. 得到 vbm 和 cbm 的信息 -- band, kpoint, spin
    vbm_dict = report_object.get_vbm(out_fermi_path=out_fermi_path)
    cbm_dict = report_object.get_cbm(out_fermi_path=out_fermi_path)
    #print(vbm_dict)
    #print(cbm_dict)
    
    
    ### Step 5. Summary
    print_sum(
            bandgap_type=bandgap_type,
            bandgap=bandgap,
            vbm_dict=vbm_dict,
            cbm_dict=cbm_dict,
            )
        
    

def print_sum(
            bandgap_type:str,
            bandgap:float,
            vbm_dict:Dict[str, Union[str, int]],
            cbm_dict:Dict[str, Union[str, int]],
            ):
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输入文件:", end="\t")
    print(" - {0}".format("REPORT"))
    print(" \t\t\t - {0}".format("OUT.FERMI"))
    
    print("\t* 输出信息:")
    print(" \t\t - 带隙类型:   {0}".format(bandgap_type))
    print(" \t\t - 带隙大小:   {0} eV".format(bandgap))
    for idx_vbm in range(len(vbm_dict["kpts"])):
        print(" \t\t - VBM on:     Band {0}, KPOINT {1}, SPIN {2}".format(
                            vbm_dict["bands"][idx_vbm],
                            vbm_dict["kpts"][idx_vbm],
                            vbm_dict["spins"][idx_vbm]
        ))
    for idx_cbm in range(len(cbm_dict["kpts"])):
        print(" \t\t - CBM on:     Band {0}, KPOINT {1}, SPIN {2}".format(
                            cbm_dict["bands"][idx_cbm],
                            cbm_dict["kpts"][idx_cbm],
                            cbm_dict["spins"][idx_cbm]
        ))
    
    print("*{0:-^68}*".format("---------"))
    

def print_sum_metal():
    print("*{0:-^68}*".format(" Summary "))
    
    print("\t* 输入文件:", end="\t")
    print(" - {0}".format("REPORT"))
    print(" \t\t\t - {0}".format("OUT.FERMI"))

    print("\t* 输出信息:")
    print(" \t\t - 带隙大小:   {0} eV".format(0))

    print("*{0:-^68}*".format("---------"))
    
    
if __name__ == "__main__":
    opt_a()