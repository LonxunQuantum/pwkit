#!/bin/bash
msubmenu5::opt4() {
  cat <<EOF
Wannier Band Interpolation (WBI) is a band structure interpolation method based on tight-binding
approximation and wannier function, which only requires a small amount of DFT calculation,
obtaining some initial k-points eigenvalues.
（基于紧束缚近似和瓦尼尔函数的插值方法，利用少量DFT计算就可以扩展得到任意的K点特征值，可以高效计算能带）
EOF

exit 0
}
