#!/bin/bash

if [ -n "$1" ]; then
	if [ -n "$2" ]; then
		echo "Восстановление из бэкапа $1..."

		echo "Распаковка..."
		unzip $1 -d ~/blogg/

		cd ~/blogg/

		echo "Восстановление статики сайта..."
		unzip static.zip

		echo "Восстановление медиа файлов сайта..."
		unzip media.zip

		echo "Восстановление записей базы данных..."
		psql -h localhost -d area51 -U $2 -W < database.dump

		echo "Очистка..."
		rm static.zip
		rm media.zip
		rm database.dump
		rm $1

		echo "Готово!"
	else
		echo "Не указано имя пользователя базы данных! Usage для кого написан был?!"

	fi
else
	echo "usage: $0 backup_filename db_username"
fi
