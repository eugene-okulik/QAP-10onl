#!/bin/bash

for i in $@; do
case `ls -l $i | cut -b 1` in
        c) echo -e "$i -- Символьное устройство" ;;
        b) echo -e "$i -- Блочное устройство" ;;
        d) echo -e "$i -- Каталог" ;;
        -) echo -e "$i -- Обычный файл" ;;
        l) echo -e "$i -- Символьная ссылка" ;;
        p) echo -e "$i -- Канал" ;;
        s) echo -e "$i -- Сокет" ;;
esac
done
