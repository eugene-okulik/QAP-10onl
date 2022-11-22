#!/bin/bash

PS3='Хотите установить python: '
echo
select choice in 'Да' 'Нет'; do
  if [[ $choice = 'Да' ]] || { echo -e 'Все равно установим'; exit 0; }; then
    echo -e 'Вы выбрали установить python' && break
  fi
done
