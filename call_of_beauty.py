from bs4 import BeautifulSoup
import sys
import argparse
import string
import random

def usage(name):
    ''' Подсказка, как запускать скрипт '''
    
    print(f'usage: {name} -i входной_файл -o выходной_файл')
    print('А теперь выйди и зайди нормально.')

def generate_random_string(size=8, chars=string.ascii_uppercase + string.digits):
    ''' Генерируем случайную строку '''

    return ''.join(random.choice(chars) for _ in range(size))

if __name__ == "__main__":
    ''' Точка входа '''
    
    parser = argparse.ArgumentParser(description='Стилизация содержимого статьи для ckeditor.')
    parser.add_argument('-i', dest='input', help='Входной файл с кодом статьи.')
    parser.add_argument('-o', dest='output', help='Имя файла с кодом, готовым к вставке.')

    args = parser.parse_args()

    ''' Проверка аргументов '''

    if not args.input or not args.output:
        usage(sys.argv[0])
        exit(0)

    file_data = ""

    ''' Открытие файла '''
    
    try:
        f = open(args.input, 'r', encoding = 'utf-8')
        file_data = f.read()
        f.close()

    except Exception as e:
        print(f'[-] Не удалось открыть файл: {e}')
        exit(1)

    ''' Переменные для обработки кода '''

    out_file_data = ""  # Выходной код
    headers = []        # Заголовки
    anchors = []        # Якоря для заголовков

    ''' Парсим html теги из файла '''

    soup = BeautifulSoup(file_data, 'html.parser')
    tags = soup.find_all()

    ''' Цикл по всем тегам, проверяем чё за тег, заменяем атрибуты '''

    for tag in tags:

        # Обработка абзаца
        if str.lower(tag.name) == 'p':

            # Обработка ссылок
            for p_link in tag.findChildren("a", recursive=False):
                p_link['class'] = 'text-danger'

            # Обрабатываем выделения в тексте
            for p_span in tag.findChildren("span", recursive=False):
                new_mark_tag = f'<mark>{p_span.text}</mark>'
                p_span = new_mark_tag

        # Обрабатываем заголовок
        elif str.lower(tag.name) == 'h1' or str.lower(tag.name) == 'h2' or str.lower(tag.name) == 'h3' or str.lower(tag.name) == 'h4' or str.lower(tag.name) == 'h5':
            headers.append(tag.text)

            anchor = str(input(f'Имя якоря для заголовка "{tag.text}": '))
            
            if anchor:
                tag['id'] = anchor
                anchors.append(anchor)

            else:
                new_id = generate_random_string()
                tag['id'] = new_id
                anchors.append(new_id)

        # Обрабатываем блок с кодом
        elif str.lower(tag.name) == 'pre':
            tag['class'] = 'mb-5 shadow-soft rounded'

        # Обрабатываем картинку
        elif str.lower(tag.name) == 'img':
            alt = tag['alt']
            url = tag['src']

            tag['class'] = 'card-img-top shadow-soft rounded'
            tag['style'] = ''
            
            new_tag = f'<a href="{url}" data-lightbox="image-1" data-title="{alt}">{tag}</a>'
            tag = new_tag

        # Обработка таблицы
        elif str.lower(tag.name) == 'table':
            del tag['align']
            del tag['border']
            del tag['cellpadding']
            del tag['cellspacing']
            del tag['style']

            tag['class'] = 'rounded shadow-soft table'

            new_tag = f'<div class="mb-5">{tag}</div>'
            tag = new_tag

        # Обработка цитаты
        elif str.lower(tag.name) == 'blockquote':
            tag['class'] = 'blockquote text-center'

            new_tag = f'<div class="row"><div style="text-align:center" class="mb-5 pt-5">{tag}</div></div>'
            tag = new_tag

        # Записываем обработанный тег
        out_file_data += str(tag)

    ''' Формируем код для содержания '''

    # html-код для содержания
    contents_code = '<li><a href="#content">Ссылка на главный заголовок</a><ul>'

    for i in range(len(headers)):
        contents_code += f'<li><a href="#{anchors[i]}">{headers[i]}</a></li>'

    contents_code += '</ul></li>'

    ''' Сохранение файла с основным кодом '''
    
    try:
        f = open(args.output, 'w', encoding='utf-8')
        f.write(out_file_data)
        f.close()

    except Exception as e:
        print(f'[-] Ошибка при сохранении файла: {e}')
        exit(1)

    ''' Сохраняем код для содержания статьи с якорями '''
    
    try:
        f = open('anchors.txt', 'w', encoding='utf-8')
        f.write(contents_code)
        f.close()

    except Exception as e:
        print(f'[-] Не удалось сохранить файл с кодом для содержания: {e}')

    print('OK')
