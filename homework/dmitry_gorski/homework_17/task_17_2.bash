#!/bin/bash

while :
do
  read -rp "Введите слово: "
  if  [[ ${REPLY} = '.' ]]; then
    echo -e 'Вы благополучно вышли' && break
  else
    if [[ ${#REPLY} -le 5 ]]; then echo -e 'Ok'; else echo -e "Слово \033[0;31m${REPLY}\033[0m слишком длинное"; fi
  fi
done
