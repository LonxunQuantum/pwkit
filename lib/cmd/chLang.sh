# 中英文切换
cmd::chLang() {
  if [ "$1" == 'cn' ] || [  "$1" == 'en' ]; then
    sed -i "s/^glanguage=.*$/glanguage=$1/" $HOME/.local/pwkit/pwkit.cfg
    echo -e "\033[32m (*_*) Change succeeded (*_*)\033[0m"
  else
    echo -e "\033[35m (*_*) Value can only be 'cn' or 'en'  (*_*)\033[0m"
  fi
}