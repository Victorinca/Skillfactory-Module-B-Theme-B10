# Skillfactory Module B. Theme B10

Completed homework for Skillfactory Course: 'Python Web Developer'. Module B - 'Introduction to Python'. Theme B10 - 'Final Project in OOP'.

## Репозиторий учебного проекта "Чат-бот в Телеграм" для курсов "Веб-разработчик на Python" и "Fullstack-разработчик на Python"
### [Модуль B. Тема B10 "Итоговый проект по ООП"](https://victorinca.github.io/Skillfactory-Module-B-Theme-B10/)

Чат-бот конвертер валют.

#### В качестве результата задания нужно написать telegram-бота на Python, в котором будет реализован следующий функционал.

1) Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).

2) При написании бота необходимо использовать библиотеку pytelegrambotapi.

3) Человек должен отправить сообщение боту в виде <имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.

4) При вводе команды /start или /help пользователю выводятся инструкции по применению бота.

5) При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.

6) Для взятия курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.

7) Для парсинга полученных ответов использовать библиотеку JSON.

8) При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.

9) Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.

10) Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента: имя валюты, цену на которую надо узнать, — base, имя валюты, цену в которой надо узнать, — quote, количество переводимой валюты — amount и возвращает нужную сумму в валюте.

11) Токен telegramm-бота хранить в специальном конфиге (можно использовать .py файл).

12) Все классы спрятать в файле extensions.py.

#### Запуск проекта

1) Создать виртуальное окружение (далее - ВО) - изолированну версию Python, которая находится у вас в папке venv:

python -m venv venv

2) Активировать ВО:

2.1) В Windows _PowerShell_ или _cmd_:

venv\sripts\activate

2.2) В Windows _GitBash_

source venv/sripts/activate

2.3) Linux, MacOS

source venv/bin/activate

3) Установить через pip

pip3 install pyTelegramBotAPI

4) Создать папку проекта и загрузить в эту папку файлы из репозитория.

#### Создание бота в Телеграм

1) В Телеграм необходимо написать @BotFather и выполнить несколько простых шагов.

2) Используйте команду /newbot, чтобы создать нового бота.

3) Установить имя (name) вашего бота. 
Имя вашего бота отображается в контактной информации и в других местах. 

4) Установить имя пользователя (username) вашего бота. 
Имя пользователя — это короткое имя, которое будет использовать для идентификации вашего бота и обращению к нему. 
Имена пользователей состоят из 5–32 символов и нечувствительны к регистру, могут включать только латинские символы, числа и символы подчеркивания. 
Имя пользователя вашего бота должно заканчиваться на "bot", например, "currency_bot" или "CurrencyBot".

5) Получить токен (token).
Токен представляет собой строку вида 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw. 
Он необходим для авторизации (подтверждения, что именно вы владелец этого бота, чтобы в программе было понятно к какому именно боту привязываются все обработчики) вашей программы, в которой реализована логика бота. 
Токен — это пароль от вашего бота, поэтому храните свой токен в безопасности!

## Поддержать, отблагодарить автора
Если представленная работа Вам понравилась, принесла пользу, сэкономила время, то Вы можете поддержать автора, воспользовавшись различными платежными системами.
- [Поддержать автора через ЮMoney](https://yoomoney.ru/to/4100117804016773)
- [Выразить признательность через Qiwi](https://qiwi.com/n/VICTORINCA)
- [Поблагодарить автора через WebMoney](https://donate.webmoney.com/w/9EVmGitMz1gusofgwT1Eof)
#### Благодарю Вас за щедрость!
#### Ваша поддержка и признательность очень приятны и важны!

## Ссылки

- [Ссылка на страницу проекта](https://victorinca.github.io/Skillfactory-Module-B-Theme-B10/)
- [Ссылка на GitHub](https://github.com/Victorinca/Skillfactory-Module-B-Theme-B10)
  
По всем вопросам, которые касаются выполненного задания, можно писать на почту victoriavladimirskaya@gmail.com.
