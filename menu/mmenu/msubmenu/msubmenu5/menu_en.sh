#!/bin/bash
submenu::5menu_en() {
  cat <<EOF
 === PWmat Module --> Electronic Structure ===
 1) Band alignment                     2) BANDUP
 3) PDOS & fatband structure           4) Wannier Band Interpolation
 5) U value calculation in LDA+U       6) High accurate k-point interpolation scheme
 7) Band structure calculation by WKM  8) Electron localization function（ELF）

 q)   Quit
 b)   Back
EOF
}
