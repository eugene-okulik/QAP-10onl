#!/bin/bash

PS3='Хотите установить Python?'
echo
select variant in "Да" "Нет"
do
if [[ $variant == "Да" ]]
then
echo "Вы выбрали установить python"
elif [[ $variant == "Нет" ]]
then
echo "Все равно установим"
fi
break
done
