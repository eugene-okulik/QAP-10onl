#!/bin/bash
enter='some text'
while [[ $enter != . ]]; do
  echo "Введите текст (для выхода введите символ '.'): "
  read enter
  if [[ ${#enter} -le 5 ]]; then
      echo "Ok"
  else echo "слово слишком длинное"
  fi
  echo
done