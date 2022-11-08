#!/bin/bash
msubmenu7::opt1() {
  cat <<EOF
This module is uesed to calculate optical absorption spectrum by rt-TDDFT method,
it is only applicable to non-periodic systems such as clusters or molecules.
For periodic systems, please refer to module 18 and module 38.
（通过rt-tddft计算非周期体系的光吸收谱，周期性体系参看module18和38）
EOF

exit 0
}
