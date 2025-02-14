"""Ответы на вопросы по виртуальному окружению.""" 

# ## Список вопроов и ответов по теме виртуальное окружение: 
#
# 1. Что делает команда python -m venv venv? 
#
# Команда для создания виртуального окружения внутри проекта. 
#
# 1.1 Что делает каждая команда в списке ниже? 
# ![png_1](https://private-user-images.githubusercontent.com/55090151/398252421-62884319-9020-4c01-a4b2-2b956a34ecab.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk1MzA5OTUsIm5iZiI6MTczOTUzMDY5NSwicGF0aCI6Ii81NTA5MDE1MS8zOTgyNTI0MjEtNjI4ODQzMTktOTAyMC00YzAxLWE0YjItMmI5NTZhMzRlY2FiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjE0VDEwNTgxNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc4NTUxMDJlMTk0NTQ3ZjRiNWM3ZWMzZDhiZTcxZWRjMmVjMjEyM2FhN2MwZThiNmVmOWU0YzQwYjY2ZTliNTkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.5zm8BJH-VKKVARUuTFncyYUa1tUXOaVTOL6Y6ODNlN8)
#
#  - pip list выводит список всех установленных пакетов в вашей текущей среде Python вместе с их версиями. 
#  - pip freeze > requirements.txt используется для создания файла requirements.txt, содержащего список всех установленных пакетов в текущей среде Python и их версий. 
#  - pip install -r requirements.txt используется для установки всех пакетов, которые прописаны в файле requirements.txt
#
# 2. Что делает каждая команда в списке ниже? 
# ![png_2](https://private-user-images.githubusercontent.com/55090151/398252102-401cc261-1400-46a9-8b24-ae650d8ce859.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzk1MzA5OTUsIm5iZiI6MTczOTUzMDY5NSwicGF0aCI6Ii81NTA5MDE1MS8zOTgyNTIxMDItNDAxY2MyNjEtMTQwMC00NmE5LThiMjQtYWU2NTBkOGNlODU5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAyMTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMjE0VDEwNTgxNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI2OTViMTM0ZjI4NWY4MzQxOTBiZjc3NzQxNDQ2NWM4MzE3ZmMwMjUyOGZkZGY4MzI3YjE2NzM1MjRlN2QxNmEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.i7SygnkwtSoixTXO9XR8ZNHJVtgyULO_uHhLFkGDENo)
#
#  - conda env list используется для отображения списка всех сред (environments), созданных с помощью conda. 
#  - conda create -n env_name python=3.5 используется для создания новой среды с указанной версией Python (в данном случае Python 3.5) с помощью менеджера пакетов conda. 
#  - conda env update -n env_name -f file.yml используется для обновления существующей среды (environment) с именем env_name с помощью файла спецификации file.yml. Файлы спецификации с расширением yml содержат информацию о зависимостях и конфигурации, которые используются для настройки среды или других процессов. 
#  - source activate env_name используется для активации указанной среды в командной оболочке. Однако начиная с версии conda 4.4, рекомендуется использовать команду conda activate env_name. 
#  - source deactivate - для деактивации виртуального окружения. С версии conda 4.4, рекомендуется использовать команду conda deactivate. 
#  - conda clean -a используется для очистки различных кешей и временных файлов, которые создаются и используются conda. Выполнение этой команды помогает освободить место на диске и поддерживать вашу систему в чистоте. 
#
# 3. Вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV" 
# ![Image](https://github.com/user-attachments/assets/5d617b01-4bfd-4652-b322-add11db90ca7) 
#
# ![Image](https://github.com/user-attachments/assets/5ac29a23-5a8a-4204-86fd-a708ffcf2bc8)
#
# 4. Как установить необходимые пакеты внутрь виртуального окружения для conda/venv? 
#
# После активации нашего окружения установить пакеты в conda можно командой conda install "package_name", в venv - pip install "package_name". 
#
# 5. Что делают эти команды?  
# ```pip freeze > requirements.txt``` - используется для создания файла requirements.txt, содержащего список всех установленных пакетов в текущей среде Python и их версий. 
# ```conda env export > environment.yml``` - используется для экспорта текущего состояния среды conda в файл спецификации environment.yml. 
#
# 5.1 Вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости 
#
# ![Image](https://github.com/user-attachments/assets/c5a5d7cb-5de4-4fdf-bd85-bf022609013d)
#
# ![Image](https://github.com/user-attachments/assets/6c18b3e0-c8b6-46e7-99f3-7c79e6c538a3)
#
# ![Image](https://github.com/user-attachments/assets/a3feaf73-143a-435d-86bf-b18912d8970d)
#
# 6. Что делают эти команды?  
# ```pip install -r requirements.txt``` - устанавливает зависимости, прописанные в файле requirements.txt. 
# ```conda env create -f environment.yml``` - устанавливает зависимости, прописанные в файле environment.yml. 
#
# 7. Что делают эти команды?  
# ```pip list``` - показывает в терминале список установленных зависимостей для интерпретатора Python с их названиями и версиями. 
# ```pip show``` - используется для отображения информации о конкретном установленном пакете в вашей текущей среде Python. 
# ```conda list``` - выводит в терминале список установленных зависимостей для интерпретатора anaconda с их названиями и версиями. 
#
# 8. Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda? 
#
# По умолчанию больше пакетов в venv/pip, чем в conda (350 тысяч против 7,5). В data science используется conda, так как этот пакетный менеджер специально предназначен для работы с большими данными, обеспечивает более эффективное управление зависимостями, поддерживает пакеты и зависимости, которые не являются Python-библиотеками. 
#
# 9. Вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor 
#
# ![Image](https://github.com/user-attachments/assets/b601cc95-7940-4cef-9a40-12abb8d5d3e4) 
#
# 10. Добавьте в .gitignore папку SENATOROV 
#
# ![Image](https://github.com/user-attachments/assets/2a928bd1-af94-4498-b9f5-0f4aaa5b3f5f)
#
# 11. Зачем нужно виртуально окружение? 
#
# Под разные проекты бывают нужны разные пакеты или разные версии одного и того же пакета. Чтобы не было конфликтов и не засорялся основной интерпретатор, для проекта создается свое виртуальное окружения и туда устанавливаются только те зависимости, которые будут в нем использоваться. 
#
# 12. С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением? 
#
# YES
#
# 13. Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda 
#
# OK
#
#

#
