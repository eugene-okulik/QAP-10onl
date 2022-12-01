#!/bin/bash

echo "Please enter a word: "
read word
while [[ "$word" != "." ]]
do
if [[ "${#word}" -le "5" ]]
then
echo "ok"
elif [[ "${#word}" -gt "5" ]]
then
echo "word is too long"
fi
echo "Please enter a word: "
read word
done
