#!/bin/bash

if [ -n "$1" ]; then
	echo "Запущено резервное копирование."

	cd ~/blogg/

	echo "Копирование файлов статики..."
	zip -r -q ./static.zip static/*

	echo "Копирование медиа файлов..."
	zip -r -q ./media.zip media/*

	echo "Создание дампа базы данных..."
	pg_dump -h localhost -d area51 -U $1 -W > database.dump

	echo "Последний штрих..."
	date=$(date '+%Y-%m-%d_%H-%M-%S')
	zip -q backup_$date.zip static.zip media.zip database.dump
	rm static.zip
	rm media.zip
	rm database.dump

	echo "Готово! Лови бэкап в корневой папке сайта."

else
	echo "usage: $0 db_username"
fi
