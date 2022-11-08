#!/bin/bash
msubmenucd::opt8() {
  cat <<EOF
In our job=SCF calculation, we have a periodic boundary condition for Poisson solution. But in a device, we can have different electrodes, which have different voltages, thus we might want to have Poisson solution with a fixed boundary values（非平衡边界条件SCF计算）
EOF

exit 0
}
