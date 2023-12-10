Задание 1. Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

Данный код представляет собой консольное приложение для работы с заметками. Разберем его по шагам:

Импорт необходимых модулей:

json - для работы с JSON-файлами. datetime - для работы с датой и временем. Определение константы NOTES_FILE, содержащей имя файла, в котором будут храниться заметки.

Функция load_notes(): Открывает файл notes.json и пытается загрузить данные из него в формате JSON. Если файл не найден, возвращается пустой список.

Функция save_notes(notes): Сохраняет переданный список заметок в файл notes.json в формате JSON с отступами.

Функция add_note(title, message): Добавляет новую заметку в список заметок, сгенерировав для нее уникальный ID и записав текущую дату и время. Затем сохраняет обновленный список заметок.

Функция list_notes(filter_date=None): Выводит список заметок. Если указана дата filter_date, то выводятся только заметки, соответствующие указанной дате.

Функция edit_note(note_id, new_title, new_message): Редактирует заметку с заданным ID, заменяя заголовок и текст заметки, а также обновляя дату и время последнего изменения.

Функция delete_note(note_id): Удаляет заметку с заданным ID из списка заметок.

Функция main(): Главная функция приложения. В бесконечном цикле запрашивает команду пользователя (add, list, edit, delete, exit) и выполняет соответствующие действия.

Запуск главной функции, только если файл запускается непосредственно (не импортируется как модуль).

Пользовательский интерфейс позволяет добавлять, просматривать, редактировать и удалять заметки. Для просмотра списка заметок можно также указать фильтр по дате. Код предоставляет основные функции для управления заметками через консоль.

Задание 2. Данное домашнее задание является продолжением домашнего задания, которое вы выполняли на предыдущем семинаре в репозитории с собственным проектом. В этом задании предлагаем каждому из вас побыть в роли тимлида.

Пригласите в свой проект кого-то из коллег по обучению, дайте им доступ к своему репозиторию (кроме ветки master).
Поставьте ему в GitHub задачу по своему проекту, попросите её выполнить в отдельной ветке, а после выполнения — создать pull request и перевести задачу обратно на вас.
Проверьте выполнение задачи, примите pull request и удалите ветку, в которой решалась данная задача.
Шаг 1: Приглашение коллеги

1.1. Заходим на свой проект "seminar1git" в GitHub.

1.2. В разделе "Settings" выбераем "Manage access".

1.3. Нажмаем "Invite a collaborator".

1.4. Вводим имя пользователя или адрес электронной почты коллеги, которого хотим пригласить, и выбераем его из списка - "colleague-username".

1.5. Выбераем уровень доступа для коллеги (write, read или admin). Например, даем ему доступ к записи, ограничив его только чтением

или предоставить права администратора (осторожно с этим).

1.6. Отправляем приглашение.

Шаг 2: Ставим задачу и создаем ветку

2.1. Создаем новую задачу в разделе "Issues" нашего проекта. Описываем задачу детально, указываем её приоритет, метки и прочую необходимую информацию.

2.2. Называем задачу осмысленным именем написать программу "Калькудятор на java" .

2.3. Назначаем задачу коллеге.

2.4. После создания задачи, переключаемся на свой локальный репозиторий.

2.5. Убедждаемся, что находимся в ветке master: git checkout master

2.6. Создаем новую ветку для выполнения задачи: git checkout -b start

2.7. Работаем в этой ветке, вносим изменения в код, добавляем новый функционал.

2.8. Зафиксируем изменения: git add . git commit -m "Калькудятор на java"

2.9. Отправляем ветку на GitHub: git push origin start

2.10. Создаем pull request на GitHub.

Шаг 3: Проверка и принятие pull request

3.1. Переходим на GitHub в раздел pull requests.

3.2. Находим созданный нашим коллегой pull request.

3.3. Внимательно просматриваем изменения в коде, оставляем комментарии, если необходимо.

3.4. Если все изменения соответствуют задаче и у нас нет замечаний, принимаем pull request.

3.5. После принятия изменений сливаем pull request в ветку master.

3.6. Удаляем ветку, в которой выполнялась задача: git branch -d start

3.7. Если ветка была удалена удаленно (remote), выполняем git push origin --delete start

Теперь наш проект обновлен, и новый функционал добавлен в ветке master.
