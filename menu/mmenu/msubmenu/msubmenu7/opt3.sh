#!/bin/bash
msubmenu7::opt3() {
  cat <<EOF
This module is used to calculate the absorption spectrum and dielectric constant using RPA method.
This module is based on second order interpolation method,
differs from PWmat utility ‘plot_ABSORB_interp.x’.
This module can give the frequency dependent dielectric function of electronic contribution,
optical properties (reflectivity, refractive index, etc.) and the macroscopic dielectric
constant ε∞ including local field effect.
（RPA方法（二阶插值）计算体材料或二维材料高频介电函数（电子部分贡献），
同时给出折射率、反射率、吸收系数等结果。另外可以给出考虑局域场效应时的宏观介电常数）
EOF

exit 0
}
