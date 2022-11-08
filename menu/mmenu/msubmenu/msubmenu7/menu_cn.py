#!/data/home/liuhanyu/anaconda3/envs/workdir/bin/python3
import click

@click.command()
def menu_cn():
  print("{0:=^80}".format(" PWmat 模块 --> 光学性质 "))
  print(
'''  1) Absorption Spectrum for non-periodic systems
 2) Absorption Spectrum Calculations for bulk systems using LDA+RPA, LDA+rt-TDDFT, HSE+rt-TDDFT methods
 3) Absorption Spectrum and dielectric constant Calculations for bulk systems using RPA method
 4) pw_absorption
 5) Raman
 6) Absorption coefficient/Extinction coefficient/Reflectivity/Refractive index/Emissivity calculations
 7) excitionic state
 8) second harmonic generation (SHG)
 9) infrared spectrum/born charge(finite electric field method)
 a) use charge density to calculate absorption spectrum for large-scale insulating systems
 b) TDDFT absorption spectrum(Linear response)

 bb) 返回上一级目录
 q)  退出
'''
)


if __name__ == "__main__":
  menu_cn()