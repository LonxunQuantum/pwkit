#!/bin/bash
submenu::5menu_cn() {
  cat <<EOF
 === PWmat 模块 --> 电子结构 ===
 1) Band alignment                     2) BANDUP
 3) PDOS & fatband structure           4) Wannier Band Interpolation
 5) U value calculation in LDA+U       6) High accurate k-point interpolation scheme
 7) Band structure calculation by WKM  8) Electron localization function（ELF）

 q)   退出
 b)   返回上一级目录
EOF
}
