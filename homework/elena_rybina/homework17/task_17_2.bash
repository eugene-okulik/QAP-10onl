#!/bin/bash
enter='some text'
while [[ $enter != . ]]; do
  echo "Введите слово: "
  read enter
  if [[ ${#enter} -le 5 ]]; then
      echo "Ok"
  else echo "Слово слишком длинное"
  fi
  echo
done
