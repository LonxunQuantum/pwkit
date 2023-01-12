import os 


def opt2():
    '''
    Description
    -----------
        1. vwr2upf.x 主要是把 PEtot 需要的 vwr 赝势格式转换为 PWmat 需要的 UPF 格式。
        2. vwr2upf.x atom.vwr，之后就会得到 atom.vwr.UPF
        
    Note
    ----
        转换之前需要对 vwr 文件进行轻微的修改，旧的 vwr 格式第一行有这
        样几个参数：nrr, icor, iatom, z, spd_loc, occ_s, occ_p, occ_d, iso，
        新的 vwr 格式需要增加截断能和相对原子质量：nrr, icor, iatom, z, spd_loc,
        occ_s, occ_p, occ_d,iso, ecut, mass。
    '''
    vwr_name = input(" 请输入vwr格式的文件名\n------------>>\n")
    os.system("echo {0} | vwr2upf.x".format(vwr_name))
    
    
if __name__ == "__main__":
    opt2()