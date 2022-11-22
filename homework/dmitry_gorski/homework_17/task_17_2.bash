#!/bin/bash

while :
do
  echo -e "Введите слово: "
  read -r user_input
  if  [[ $user_input = '.' ]]; then
    echo -e 'Вы благополучно вышли' && break
  else
    if [[ ${#user_input} -lt 5 ]]; then echo -e 'Ok' && continue; else echo -e 'Слово слишком длинное' && continue; fi
  fi
done
