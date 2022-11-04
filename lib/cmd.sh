source $PWKIT_ROOT/lib/cmd/chLang.sh

tlack="l:hH"
tlong="lang:,help"
targs=$(getopt -a -o $tlack -l $tlong -n "$(basename $0)" -- "$@") || exit 1
eval set -- "$targs"

# echo "targs: $targs"
# echo $@

parse_cmd_parameters() {
  while [ $# -gt 0 ]; do
    case "$1" in
    -h | -H | --help)
      usage
      shift
      ;;
    -l | --lang)
      cmd::chLang $2
      shift 2
      ;;
    -S | --share)
      SHAREIP="-nic shared"
      shift
      ;;
    -D | --dedicated)
      SHAREIP="-nic dedicated"
      shift
      ;;
    -i | --ip)
      POSTIP=$2
      shift 2
      ;;
    -o | --origin)
      IMMIP=$2
      shift 2
      ;;
    -n | --netmask)
      SUBNET=$2
      shift 2
      ;;
    -g | --gateway)
      GATEWAY=$2
      PREIP=${2%.*}
      shift 2
      ;;
    -s | --show)
      SHOWIP=1
      shift
      ;;
    --)
      shift
      break
      ;;
    *)
      echo -e "\033[35m (*_*) parameter error! Try Again... (*_*)\033[0m"
      exit 1
      ;;
    esac
  done
}
