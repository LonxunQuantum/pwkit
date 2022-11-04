#!/bin/bash
menu::menu_en() {
  cat <<EOF
 ===================== PWmat Module ======================
 === Material structure ===
 1) structure search                    2) disordered structure
 3) molecular dynamics data processing  4) CIF file conversion and structure processing

 === Electronic Structure and Phonon Calculation ===
 5) Electronic Structure                6) Phonon Calculation

 === Optical, magnetic, mechanical and polarization properties ===
 7) Optical properties                  8) Magnetic properties
 9) Mechanical properties               a) Polarization property

 b) Defect nature                c) Electrochemical properties
 d) Transport property           e) Ultrafast dynamic process
 f) Beyond DFT                   g) Electron beam irradiation decomposition
 h) Large system computing       i) Machine learning force field
 j) other

 ===================== PWmat 插件 ======================
 k) Format conversion      l) Data visualization      m) Data post-processing

 q)  Quit
EOF
}
