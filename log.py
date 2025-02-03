"""Log-файл уроков @SENATOROVAI."""

# 03/02/2025
#
# ### Регистрация аккаунтов
#
# 1. GitHub
#     - git - система контроля версий
#     - github - удалённый хостинг для хранения и совместной разработки проектов
#     - шаблоны профиля на github (название репозитория = имя пользователя)
#     - отправил в Flood ссылку на свой [профиль](https://github.com/tigermun)
#
# 2. Kaggle
#     - объединение учёных математиков и программистов со всего мира
#     - крупнейшая международная платформа соревнований по Data Science
#     - регистрация через канадский номер (арендовал [здесь](https://365sms.pro/))
#     - получил статус контрибьютора (участник проекта, помощник, содействующий)
#     - подписался на коллег на платформе
#     - отправил в Flood ссылку на свой [профиль](https://www.kaggle.com/tagirenikeev)
#
# 3. ODS
#     - Open Data Science
#     - открытое сообщество специалистов и любителей данных
#     - отправил в Flood ссылку на свой [профиль](https://ods.ai/users/r30e3344c8f75)
#
#
# ### Скачивание и установка программ
#
# 1. GitHub Desktop
#     - клиент github для работы с удалёнными репозиториями
#
# 2. Cursor и VS CODE
#     - редакторы кода
#     - VSCode уже был
#     - чтобы из ```GitHub Desktop``` можно было переходить в ```cursor```: ```File -> Options -> Integrations```, в выпадающем списке ```external editor``` выбираешь ```cursor``` и сохраняешь настройку
#
# 3. Установка плагинов в VSCode:
#     - ms-python.pylint
#     - ms-python.flake8
#     - ms-python.mypy-type-checker
#     - matangover.mypy
#     - ms-pyright.pyright
#     - ms-python.black-formatter
#     - njpwerner.autodocstring
#     - njqdev.vscode-python-typehint
#     - KevinRose.vsc-python-indent
#     - mintlify.document
#     - streetsidesoftware.code-spell-checker
#     - eamodio.gitlens
#     - ms-toolsai.jupyter
#     - ms-vsliveshare.vsliveshare
#     - njqdev.vscode-python-typehint
#     - EricSia.pythonsnippets3
#     - ms-pyright.pyright
#     - congyiwu.vscode-jupytext
#     - streetsidesoftware.code-spell-checker-russian
#
# 4. подготовка VSCode к работе
#     - автосохранение (file -> auto save)
#     - длина строки в файле
#         settings -> editor -> word wrap: wordWrap
#         settings -> editor -> word wrap: wordWrapColumn = 79
#     - про перенос переменной новую строку, если не хватает длины строки
#     - строку можно разделить на подстроки и держать в круглых скобках
#         s = ('первая часть строки '
#              'вторая часть строки')
#     - PROBLEMS
#     - коммит через соответствующую вкладку VSCode
#     - разделение экрана VSCode на несколько частей для удобства работы с несколькими файлами одновременно
#     - [возможности курсора](https://www.youtube.com/watch?v=hjBCRVYE1as) впечатляют
#
# 5. Python (CPython)
#     - скачал, обновил уже имеющийся
#
# 6. Git for Windows
#     - скачал, обновил уже имеющийся
#
# 7. Conda
#     - скачал Miniconda, установил
#     - скачал Anaconda, установил
#
# 8. Джамборд для учёбы
#     - зарегался на сайте [canva](https://www.canva.com/) с помощью ```cloud vpn``` с локацией Канада
#     - сделал по [инструкции](https://youtu.be/8pwKgbMyfbo)
#     - в личку преподавателю скинул ссылку на свой ноутбук на ```canva```
#
# ### Скачать репозиторий на свой компьютер
#
# 1. создал свою ветку в [репе](https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-SENATOROV)
# 2. клонировал репозиторий
# 3. конкретную ветку клонировать не стал
#     ```bash
#     git clone --branch название-ветки https://github.com/SENATOROVAI/Data-Science-For-Beginners-from-scratch-SENATOROV.git
#     cd Data-Science-For-Beginners-from-scratch-SENATOROV
#     cursor .
#     ```
# 4. в терминал VSCode ввёл:
#     ```bash
#     git init
#     pip install pre-commit
#     pre-commit install
#     pre-commit run --all-files
#     ```
# 4. отправил скриншот терминала в чат
# 5. в корне проекта создал файл ```log.ipynb```
