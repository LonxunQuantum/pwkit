# image class, again, hahaha
# all forces in python variables are correct one f_atom = -dE/dR
# please add minus sign when you read and write MOVEMENT
import numpy as np
import numpy.linalg as LA
import matplotlib
import matplotlib.pyplot as plt
import sys
import dpdata
import os
import argparse

element = ["0", "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg"]

class Image():
    def __init__(self, num_atoms, lattice, type_atom, x_atom, f_atom, e_atom, ddde, e_potential):
        self.num_atoms = num_atoms
        self.lattice = lattice
        self.type_atom = type_atom
        self.x_atom = x_atom
        self.f_atom = f_atom
        self.e_atom = e_atom
        self.e_potential = e_potential
        self.ddde = ddde

        self.egroup = np.zeros((num_atoms), dtype=float)
        
    # This member function won't be used in modifying MOVEMENT
    def calc_egroup(self):
        # to line 40, get e_atom0
        f = open(r'fread_dfeat/feat.info', 'r')
        txt = f.readlines()
        f.close()
        iflag_pca = int(txt[0].split()[0])
        num_feat_type = int(txt[1].split()[0])
        for i in range(num_feat_type):
            ifeat_type = int(txt[2+i].split()[0])
        num_atomtype = int(txt[2+num_feat_type].split()[0].split(',')[0])
        itype_atom = np.zeros((num_atomtype), dtype=int)
        nfeat1 = np.zeros((num_atomtype), dtype=int)
        nfeat2 = np.zeros((num_atomtype), dtype=int)
        nfeat2_integral = np.zeros((num_atomtype), dtype=int)
        nfeat = np.zeros((num_feat_type, num_atomtype), dtype=int)
        ipos_feat = np.zeros((num_feat_type, num_atomtype), dtype=int)
        for i in range(num_atomtype):
            tmp = [int(kk) for kk in txt[3+num_feat_type+i].split()]
            itype_atom[i] = tmp[0]
            nfeat1[i] = tmp[1]
            nfeat2[i] = tmp[2]
        for i in range(num_atomtype):
            nfeat2_integral[i] = np.sum(nfeat2[0:i+1])

        # read fit_linearMM.input
        f = open(r'fread_dfeat/fit_linearMM.input', 'r')
        txt = f.readlines()
        f.close()
        tmp_ntype = int(txt[0].split()[0].split(',')[0])
        tmp_m_neigh = int(txt[0].split()[1].split(',')[0])
        type_map = [ 0 for i in range(tmp_ntype)]
        for i in range(tmp_ntype):
            type_map[i] = int(txt[1+i].split()[0].split(',')[0])

        dwidth = float(txt[tmp_ntype+2].split()[0])

        # read linear_fitB.ntype
        f = open(r'fread_dfeat/linear_fitB.ntype', 'r')
        txt = f.readlines()
        f.close()
        e_atom0 = np.zeros((num_atomtype), dtype=float)
        for i in range(num_atomtype):
            e_atom0[i] = float(txt[nfeat2_integral[i]].split()[1])

        # calc distance
        # num_atoms, x_atom, lattice
        distance_matrix = np.zeros((self.num_atoms, self.num_atoms), dtype=float)
        for i in range(self.num_atoms):
            d0 = self.x_atom - self.x_atom[i]
            d1 = np.where(d0<-0.5, d0+1.0, d0)
            dd = np.where(d1>0.5, d1-1.0, d1)
            d_cart = np.matmul(dd, self.lattice)
            distance_matrix[i] = np.array([ LA.norm(kk) for kk in d_cart])

        fact_matrix = np.exp(-distance_matrix**2/dwidth**2)
        e_atom0_array = np.zeros((self.num_atoms), dtype=float)
        for i in range(self.num_atoms):
            e_atom0_array[i] = e_atom0[type_map.index(self.type_atom[i])]

        for i in range(self.num_atoms):
            esum1 = ((self.e_atom - e_atom0_array)*fact_matrix[i]).sum()
            self.egroup[i] = esum1 / fact_matrix[i].sum()

def write_image(fout, image):
    fout.write(" %d atoms, Iteration (fs) = %16.10E, Etot,Ep,Ek (eV) = %16.10E  %16.10E   %16.10E\n"\
                % (image.num_atoms, 0.0, image.e_potential, image.e_potential, 0.0))
    fout.write(" MD_INFO: METHOD(1-VV,2-NH,3-LV,4-LVPR,5-NHRP) TIME(fs) TEMP(K) DESIRED_TEMP(K) AVE_TEMP(K) TIME_INTERVAL(fs) TOT_TEMP(K) \n")
    fout.write("          1    0.5000000000E+00   0.59978E+03   0.30000E+03   0.59978E+03   0.50000E+02   0.59978E+03\n")
    fout.write(" MD_VV_INFO: Basic Velocity Verlet Dynamics (NVE), Initialized total energy(Hartree)\n")
    fout.write("          -0.1971547257E+05\n")
    fout.write("Lattice vector (Angstrom)\n")
    for i in range(3):
        fout.write("  %16.10E    %16.10E    %16.10E\n" % (image.lattice[i][0], image.lattice[i][1], image.lattice[i][2]))
    fout.write("  Position (normalized), move_x, move_y, move_z\n")
    for i in range(image.num_atoms):
        fout.write(" %4d    %20.15F    %20.15F    %20.15F    1 1 1\n"\
                 % (image.type_atom[i], image.x_atom[i][0], image.x_atom[i][1], image.x_atom[i][2]))
    fout.write("  Force (-force, eV/Angstrom)\n")
    for i in range(image.num_atoms):
        fout.write(" %4d    %20.15F    %20.15F    %20.15F\n"\
                 % (image.type_atom[i], -image.f_atom[i][0], -image.f_atom[i][1], -image.f_atom[i][2]))  # minus sign here
    fout.write("  Atomic-Energy, Etot(eV),E_nonloc(eV),Q_atom:dE(eV)=  %20.15E\n " % image.ddde)
    for i in range(image.num_atoms):
        fout.write(" %4d    %20.15F    %20.15F    %20.15F\n"\
                 % (image.type_atom[i], image.e_atom[i], 0.0, 0.0))
    fout.write(' -------------------------------------\n')
    # idtk = i don't know


def outcar2raw():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='specify input movement filename', type=str, default='OUTCAR')
    parser.add_argument('-n', '--number', help='specify number of samples per set', type=int, default=2000)
    parser.add_argument('-d', '--directory', help='specify stored directory of raw data', type=str, default='.')
    args = parser.parse_args()

    dpdata.LabeledSystem(args.input, fmt='vasp/outcar').to('deepmd/raw', args.directory)

if __name__ == '__main__':

    outcar2raw() 
    print("raw dar extracted from outcar\n")
    type_raw = np.loadtxt(r'type.raw', dtype=int)
    box_raw = np.loadtxt(r'box.raw')
    coord_raw = np.loadtxt(r'coord.raw')
    energy_raw = np.loadtxt(r'energy.raw')
    force_raw = np.loadtxt(r'force.raw')
    fin = open(r'type_map.raw')
    type_map_txt = fin.readlines()
    fin.close()

    print ("raw data reading completed\n")	
    num_type = len(type_map_txt)
    num_atom = type_raw.shape[0]
    num_image = coord_raw.shape[0]
    type_map = [ 'H' for tmp in range(num_type)]
    type_atom = np.zeros((num_atom), dtype=int)

    for i in range(num_type):
        type_map[i] = type_map_txt[i].split()[0]
    for i in range(num_atom):
        type_atom[i] = element.index(type_map[type_raw[i]])

    all_images = []
    for i in range(num_image):
        lattice = box_raw[i].reshape(3,3)
        x_atom = np.dot(coord_raw[i].reshape(num_atom,3),LA.inv(lattice))
        f_atom = force_raw[i].reshape(num_atom,3)
        tmp_eatom = energy_raw[i] / num_atom
        e_atom = np.array([tmp_eatom for i in range(num_atom)])
        ddde = 0.0
        e_potential = energy_raw[i]
        tmp_image = Image(num_atom, lattice, type_atom, x_atom, f_atom, e_atom, ddde, e_potential)
        all_images.append(tmp_image)

    fout = open('MOVEMENT', 'w')
    for i in range(num_image):
        write_image(fout, all_images[i])
    fout.close()
