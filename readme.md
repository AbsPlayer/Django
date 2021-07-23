Django test project.

Advertisement board.

Used:

- classes View and generic views(ListView and DetailView etc)
- AdvertisementInLine for advertisements in admin panel
- 2 part of site - advertisements and authors
- html-layouts for site parts
- internationalization
- collapse for contacts users in admin panel
- thumbnails for advertisements preview
- captcha to user login
- search in advertisements rubrics
- bootstrap
- django templates tags for html
- there are 3 advertisements status (see settings.py) and so there are 3 actions in admin panel for bulk processing of advertisements
- advertisement author = user, but user is not always author. E.g. superuser of site is not author by default. So there are relevant messages in site

===

Тестовий проект на Django.

Дошка оголошень.

Використано:

- класи View і generic views(ListView, DetailView тощо)
- AdvertisementInLine для оголошень в адмін-панелі
- 2 частини сайту - оголошення та автори
- html-шаблони частин сайту
- інтернаціоналізація
- згортання для контактів користувачів в адмін-панелі
- thumbnails для прев'ю оголошень
- капча при залогіненні користувача
- пошук в рубриках оголошень
- bootstrap
- шаблонні теги django для html    
- є 3 статуси оголошень (див. settings.py) і відповідно 3 дії в адмін-панелі для масової обробки оголошень
- автор оголошення = користувач, але користувач не завжди є автором. Наприклад, superuser сайта не є автором за замовчуванням. Отже є відповідні повідомлення на сайті 