#!/bin/bash

echo "Введите слово: "
read word
while [[ "$word" != "." ]]
do
if [[ "${#word}" -le "5" ]]
then
echo "ok"
elif [[ "${#word}" -gt "5" ]]
then
echo "Слово слишком длинное"
fi
echo "Введите слово: "
read word
done
