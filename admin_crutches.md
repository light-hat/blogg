# Стилизация статьи

Вообще это был временный файл, где я помечал себе, как менять код, выдаваемый сkeditor так, чтобы содержимое статьи смотрелось гармонично со стилем всего сайта. Сначала я это делал руками, потом создал для этого скрипт `call_of_beauty.py`. В общем этот файл теперь рудимент, но тут написано, как именно скрипт меняет код статьи. Может зачем-то пригодится.

## Содержание

### Само содержание

Поле под WYSIWYG редактором - там прописана разметка содержания статьи.

```
<li>
<a href="#content">Ссылка на главный заголовок</a>
    <ul>
		<li><a href="#link">Заголовок в статье</a></li>
		<li><a href="#link">Заголовок в статье 1</a></li>
		<li><a href="#link">Заголовок в статье 2</a></li>
			<ul>
				<li><a href="#link">Подзаголовок</a></li>
				<li><a href="#link">Подзаголовок 1</a></li>
				<li><a href="#link">Подзаголовок 2</a></li>
				<li><a href="#link">Подзаголовок 3</a></li>
			</ul>

		<li><a href="#link">Заголовок в статье 3</a></li>
    </ul>
</li>
```

Здесь вместо `#link` прописываем `id` заголовка, к которому хотим переместиться.

Внутри `a` мы прописываем его название.

Чтобы у пункта были дочерние пункты, мы создаём внутри тега `li` список `ul`, элементы которого оформляем по тому же принципу, что и родительский.

### Порядок стилизации заголовков

Когда оформляем заголовок, указываем следующее:

```
<h2 id="#link">...</h2>
```

`#link` мы указываем для каждого заголовка уникальный, чтобы сайт знал, в какое место перемещаться и всё работало так, как нужно.

Совет: делать их в последнюю очередь, так как присвоенные в source коде айдишники при переходе к предпросмотру сбрасываются.

## Основные элементы страницы

Речь пойдёт об:
- Таблицах
- Картинках
- Вставках кода
- Ссылках
- Цитатах


### Таблица
```
<div class="mb-5">
<table class="rounded shadow-soft table">
	<tbody>
		<tr>
			<th scope="col">Class</th>
			<th scope="col">Teacher</th>
			<th scope="col">Males</th>
			<th scope="col">Females</th>
		</tr>
		<tr>
			<th rowspan="2" scope="row">First Year</th>
			<th scope="row">D. Bolter</th>
			<td>5</td>
			<td>4</td>
		</tr>
		<tr>
			<th scope="row">A. Cheetham</th>
			<td>7</td>
			<td>9</td>
		</tr>
		<tr>
			<th rowspan="3" scope="row">Second Year</th>
			<th scope="row">M. Lam</th>
			<td>3</td>
			<td>9</td>
		</tr>
		<tr>
			<th scope="row">S. Crossy</th>
			<td>4</td>
			<td>3</td>
		</tr>
		<tr>
			<th scope="row">A. Forsyth</th>
			<td>6</td>
			<td>9</td>
		</tr>
	</tbody>
</table>
</div>
```

Напоминаю:
- `tr` - строка таблицы (row, ряд)
- `th` - заголовок строки/столбца
- `td` - ячейка таблицы для опр. столбца

### Картинка

#### Большая картинка

В общем, по началу загружаем картинку так, как нам предлагает редактор. Получаем примерно такой код для картинки:
```
<p><img alt="Это пример скриншота" src="/media/uploads/2022/01/27/screenshot-887.png" style="height:300px; width:533px" /></p>
```

Меняем его на примерно это:
```
<img alt="Это пример скриншота" src="/media/uploads/2022/01/27/screenshot-887.png" class="card-img-top shadow-soft rounded"/>
```

#### Маленькая картинка

Было:
```
<p style="text-align:center"><img alt="Картинка поменьше" src="/media/uploads/2022/01/27/1546164454195250154.jpg" style="height:565px; width:400px" /></p>
```

Стало:
```
<p style="text-align:center"><img class="card-img-top shadow-soft rounded" alt="Картинка поменьше" src="/media/uploads/2022/01/27/1546164454195250154.jpg" style="height:565px; width:400px" /></p>
```

Картинка с лайтбоксом:
```

<p style="text-align:center">
	<a href="/media/uploads/2022/01/27/1546164454195250154.jpg" data-lightbox="image-1" data-title="Картинка поменьше">
		<img class="card-img-top shadow-soft rounded" alt="Картинка поменьше" src="/media/uploads/2022/01/27/1546164454195250154.jpg" style="height:565px; width:400px" />
	</a>
</p>

```

`data-lightbox` можем не менять, так картинки можно будет листать.

### Код
Было:
```
<pre>
<code class="language-bash">$ ls -la | grep flag</code></pre>
```

Стало:
```
<pre class="mb-5 shadow-soft rounded">
<code class="language-bash">$ ls -la | grep flag</code></pre>
```

`Примечание`: атрибуты тега сбиваются при выходе из режима редактирования кода (так же, как и заголовки).

### Ссылки
Пример ссылки.
```
<a href="https://ru.lipsum.com/" class="text-danger">Text of the link</a>
```

Цвета:
- Черный: text-default
- Синий: text-secondary
- Красный: text-danger
- Зелёный: text-success
- Голубоватый: text-info
- Серый: text-gray

### Цитаты
Вставляем их примерно так:
```
<div class="row"><div style="text-align:center" class="mb-5 pt-5 col-md-10"><blockquote class="blockquote text-center">
Хороший человек плохой воздух в себе держать не будет
<footer class="blockquote-footer mt-3 text-dark">Джейсон Стейтем</footer>
</blockquote></div></div>
```
