"""chapter_1."""

# # Chapter 1 Introduction to Data Science and Programming Basics
#
# ## What is Data Science?
#
# <p> Философский спор о первичности духовного и материального не был разрешен.
# <p> Теперь сюда добавилась третья величина - **информация / данные.**
# <p> Data Science - это  наука об изучении данных для того, что бы данные обрели смысл и дали полезную информацию.
# <p> История Data Science. 18000 г. до н.э. до наших времен.
#
# **Предметные области входящие в Data Science:**
# 1. Математика, статистика и алгоритмы.
# 2. Знание бизнеса и предметной области. Сбор данных.
# 3. Программирование. Машинное обучение. ИИ. Глубокое обучение.
#
# Математика — это точная формальная наука, первоначально исследовавшая количественные отношения и пространственные формы. В более современном понимании это наука об отношениях между объектами, о которых ничего не известно, кроме описывающих их некоторых свойств. Именно эти свойства в качестве аксиом положены в основание той или иной математической теории.
#
# Стати́стика — отрасль знаний, наука, в которой излагаются общие вопросы сбора, измерения, мониторинга, анализа массовых статистических (количественных или качественных) данных и их сравнение; изучение количественной стороны массовых общественных явлений в числовой форме.
#
# Алгоритм — это точно определённая инструкция, последовательно применяя которую к исходным данным, можно получить решение задачи. Для каждого алгоритма есть некоторое множество объектов, допустимых в качестве исходных данных. Например, в алгоритме деления вещественных чисел делимое может быть любым, а делитель не может быть равен нулю. Алгоритм служит, как правило, для решения не одной конкретной задачи, а некоторого класса задач.
#
# Сбор данных - это процесс получения информации, относящейся к вашему исследовательскому вопросу или гипотезе. Это может включать в себя множество разных методов, включая наблюдение, опросы, интервью и изучение документов. Следовательно для построения правильной гипотезы необходимо знать предметную область исследования.
#
# Синегетический эффект взаимодействия предметных областей позволяет объектно ориентировано извлекать информацию из огромных обьемов данных с использованием различных научных методов, алгоритмов и процессов, обнаруживать скрытые закономерности в необработанных данных.
#
# **Перспективные профессиональные сферы с этим набором компетенций — AI, ML, DL.**
# Рассмотрим их подробнее и разберёмся, как эти понятия связаны между собой.
#
# Artificial Intelligence, или AI (с англ. «искусственный интеллект») — создание и развитие систем, которые способны решать интеллектуальные задачи. Например, такие системы могут распознавать симптомы болезней на медицинских снимках или играть в шахматы с человеком. В основе технологий искусственного интеллекта лежит работа с большими данными. С помощью различных методов специалисты создают алгоритмы, которые имитируют человеческое мышление.
#
# Искусственный интеллект — большая область знаний и технологических практик. В ней выделяют разделы: машинное и глубокое обучение. Их методы используют для решения основной задачи Data Science — извлечь из данных пользу для людей и бизнеса
#
# Machine Learning, или ML (с англ. «машинное обучение») — это раздел AI, который сфокусирован на обучении компьютерных систем таким образом, чтобы они могли решать задачи и делать прогнозы на основе данных. Например, предсказать погоду на месяц на основе метеорологических наблюдений за предыдущие 10 лет. На технологиях машинного обучения построены рекомендательные алгоритмы на стриминговых платформах вроде Кинопоиска и Яндекс Музыки. Чтобы предлагать пользователям контент, который с наибольшей вероятностью им понравится, программы обрабатывают данные о прослушиваемых треках и просматриваемых фильмах и на их основе подбирают рекомендации.
#
# Для машинного обучения используют модели — программы, которые основаны на алгоритмах, например деревья решений и линейная регрессия. В модель загружают большие данные и запускают обучение: программа анализирует информацию и работает с ней по заданному алгоритму.
#
# Deep Learning, или DL (с англ. «глубокое обучение») — это более сложный вид машинного обучения. В его основе нейронные сети — математические модели со множеством элементов: узлов и слоёв. Для глубокого обучения нужно ещё больше данных, чем для машинного. Но и в результате система может решать более сложные задачи. Например, распознавать голоса и объекты на изображениях, анализировать текст и генерировать ответы на запросы пользователей. Технологии глубокого обучения использовали для создания, например, ChatGPT, YaGPT и Midjourney.
#
# **Основные этапы работы с данными**
#
# В крупных компаниях проект Data Science часто реализует большая команда из разных IT-специалистов. Дата-инженеры, аналитики данных и дата-сайентисты подключаются на разных этапах работы. В среднем и малом бизнесе обычно ищут специалиста-универсала.
#
# Независимо от размера компании и проекта дата-сайентисту нужно последовательно решить несколько рабочих задач до того, как построить модель. Условно работу над проектом Data Science можно разделить на четыре больших этапа:
#
# <p> 1. Составить требования к данным
# Сначала определяют цель проекта. Например, компании нужно прогнозировать спрос на товары: когда и что покупают чаще. Это позволит не закупать у поставщиков больше, чем получится продать, и так снизить затраты.
#
# Чтобы понять, какие данные помогут в достижении цели, важно изучить предметную область: рынок, конкурентов, организацию работы компании. Далее требования к данным собирают в техзадание для заказчика.
#
# <p> 2. Подготовить данные
# Допустим, дата-сайентисту передали данные о заказах за предыдущие 10 лет. Теперь нужно убедиться, что они подходят для обучения модели.
#
# Данные чистят от ошибок, например продублированных значений, пропусков, опечаток и аномалий. Проводят разведочный анализ данных, или EDA (сокр. от Exploratory data analysis), — ищут закономерности и отклонения, связи и зависимости между переменными, чтобы учесть их при обучении модели. Для этого используют различные методы, например факторный, корреляционный и кластерный анализ.
#
# <p> 3. Найти решение
# Исходя из задачи, нужно подобрать подходящий подход для её решения. На этом этапе нужны знания о том, с какими данными и как работают разные модели машинного обучения, какой результат дают.
#
# Например, линейная регрессия предскажет спрос на товар. Но только если между факторами, которые влияют на этот спрос, линейная связь. Если это не так — лучше использовать иные модели. Можно сразу выбрать несколько моделей, чтобы протестировать их и сравнить результаты.
#
# После выбора подхода формируют выборку, на которой будет обучаться модель.
#
# <p> 4. Построить модель
# На этом этапе строят и обучают модели. Затем проверяют корректность работы на небольшом количестве реальных данных. Если модель не сработает, корректируют параметры обучающей выборки или вообще выбирают новую модель и формируют другую выборку данных.
#
# ## От Data Science к программированию.
#
# **Программирование** - это идеи, преобразованные в пошаговые инструкции, понятные компьютеру.
#
# Такая пошаговая инструкция называется **алгоритм**.
# Алгоритм - пошаговая процедура, конечная последовательность четко определенных, реализуемых компьютером инструкций для решения какой-то проблеммы или для выполнения вычислений.
# Алгоритмы состоят из трех видов операторов. которые могут присутсвовать в различных комбинациях:
# Последовательные операторы
# Условные операторы
# Цикл и итерации
#
# **Блок-схемы** - это алгоритмы изображенные в графической форме.
# Блок-схема — это схематичное представление процесса, системы или компьютерного алгоритма.
# Блок-схемы часто применяются в разных сферах деятельности, чтобы документировать, изучать, планировать, совершенствовать и объяснять сложные процессы с помощью простых логичных диаграмм.
# Для построения блок-схем применяются прямоугольники, овалы, ромбы и некоторые другие фигуры (для обозначения конкретных операций), а также соединительные стрелки, которые указывают последовательность шагов или направление процесса.
# Символы для составления блок-схем стандартны.
#
# В блок-схемах чаще всего встречаются следующие фигуры и символы.
#
# | Символ | Название символа |Описание|
# | ----------- | ----------- |----------- |
# || «Процесс» |Этот символ, также известный под названием «Действие», используется для обозначения процесса, действия или функции.|
# || «Начало/конец» |Данный символ, который иногда также именуют «Терминатором», применяется для обозначения начальной или конечной точки схемы или возможного результата того или иного пути развития процесса. Внутри блока, как правило, располагается слово «Начало» или «Конец».|
# || «Документ» |Символизирует ввод или вывод документа. Под вводом документа может подразумеваться поступление отчета, электронного письма или заказа. Примеры вывода документов: создание презентации, рабочего конспекта или письма. |
# || «Решение» |Символизирует вопрос, на который требуется ответ (как правило, «да/нет» или «истина/ложь»). На этом этапе блок-схема разветвляется в разных направлениях в зависимости от выбранного ответа и последующих блоков.|
# || «Соединитель» |Обычно применяется в более сложных схемах для соединения отдельных блоков в пределах одной страницы. |
# || «Межстраничный соединитель»| Часто применяется в сложных схемах для соединения отдельных блоков, расположенных на разных страницах. Для удобства интерпретации внутри фигуры, как правило, указывается номер страницы.|
# || «Ввод/вывод» | Эта фигура, также известная под названием «Данные», символизирует данные, доступные для ввода или вывода, а также затраченные или полученные ресурсы. Хотя «Бумажная лента» также означает ввод/вывод данных, на сегодняшний день этот символ считается устаревшим и потому довольно редко используется в блок-схемах.|
# || «Комментарий» |В сочетании с другими материалами этот символ позволяет добавить необходимый контекст, разъяснение или комментарий к определенному диапазону данных. Комментарий также можно присоединить к необходимому разделу блок-схемы с помощью пунктирной линии. |
#
# **Более сложные символы для блок-схем**
# Эти дополнительные символы в основном применяются при создании схем технологических процессов для приложений, карт пути пользователя, обработки данных и так далее.
#
# | Символ | Название символа |Описание|
# | ----------- | ----------- |----------- |
# || «База данных»  |Символизирует данные, хранимые на сервисе, где, вероятнее всего, допускается поиск и фильтрация.|
# || «Бумажная лента» | Устаревший символ, который редко используется в современной практике и схемах процессов. Тем не менее, «бумажную ленту» можно использовать при схематизации процессов или способов ввода на старых компьютерах и системах ЧПУ.|
# ||Точка суммирования  |Суммирует содержимое объединяющихся процессов.|
# || Предопределенный процесс (подпрограмма)	 |Символизирует сложные процессы и операции, которые уже известны или охарактеризованы в другом месте.|
# || «внутренняя память» |Эта фигура часто применяется в проектировании программного обеспечения и символизирует данные, хранящиеся во внутренней памяти. |
# || «ручной ввод» |Символизирует ручной ввод данных в поле или в ходе выполнения шага (как правило, посредством клавиатуры или иного устройства). Примером такого сценария может послужить процесс входа в систему, при котором пользователю нужно ввести свои учетные данные вручную. |
# || «ручная операция» |Символизирует шаг, который подлежит выполнению вручную, а не автоматически. |
# || «слияние»| Указывает на слияние нескольких процессов в один.|
# || «документы» |Символизирует несколько документов или отчетов. |
# ||«подготовка»  | Позволяет разграничивать шаги, направленные на подготовку к работе, и шаги непосредственно по выполнению работы. Помогает внедрить конфигурацию в другой шаг в рамках того же процесса.|
# ||  «хранимые данные»| Эта фигура также носит название «Хранилище данных» и применяется для обозначения места хранения данных в пределах процесса.|
# ||  «задержка»| Символизирует сегмент процесса, где наблюдается промедление. Рекомендуем указать длительность задержки внутри фигуры.|
# ||  «или»| Как видно из названия, эта фигура указывает, что после этой точки течение процесса идет двумя или более путями.|
# ||  «вывод на экран»| Позволяет указать, на каком этапе процесса информация будет отображаться на экране. |
# || «жесткий диск»|Указывает, где на жестком диске хранятся данные. Другое название — «Хранилище прямого доступа».|
#
# **Что такое языки програмирования?**
#
# Язык программирования — это формальная знаковая система, на которой пишут компьютерные программы. Его можно представить как набор разнообразных правил и команд, на основе которых программист пишет код.
# Машинный язык.
# Языки высокого уровня.
# исходный код.
# Компилятор - программа преобразующая исходный код в машинный.
# Интерпретатор - программа, которая непосредственно выполняет инструкции, написанные на языке программирования. безх предварительной компиляции в программу на машинном языке.
# IDE (Integrated Development Environment) интегрированная среда разработки.
#

# # 1.5. Упражнения

# 1.5.1. Какие предметные области входят в Data Science?
# <p> В Data Science входят: математика, статистика, программирование, машинное обучение, системный анализ предметной области (бизнеса).
# <p> Что между ними общего и в чем различие?
# Направления Data Science:
# <p> Artificial Intelligence, или AI (с англ. «искусственный интеллект») — создание и развитие систем, которые способны решать интеллектуальные задачи. Это пока не существует.
# Искусственный интеллект — большая область знаний и технологических практик. В ней выделяют разделы: машинное и глубокое обучение. Их методы используют для решения основной задачи Data Science — извлечь из данных пользу для людей и бизнеса
# <p> Machine Learning, или ML (с англ. «машинное обучение») — это раздел AI, который сфокусирован на обучении компьютерных систем таким образом, чтобы они могли решать задачи и делать прогнозы на основе данных.
# <p>Deep Learning, или DL (с англ. «глубокое обучение») — это более сложный вид машинного обучения. В его основе нейронные сети — математические модели со множеством элементов: узлов и слоёв. Для глубокого обучения нужно ещё больше данных, чем для машинного. Но и в результате система может решать более сложные задачи.
#
# 1.5.2. Как вы понимаете термин "алгоритм"?
# <p> Алгоритм — это точно определённая инструкция, последовательно применяя которую к исходным данным, можно получить решение задачи.
# <p> Алгоритм - пошаговая процедура, конечная последовательность четко определенных, реализуемых компьютером инструкций для решения какой-то проблеммы или для выполнения вычислений.
# <p> Как алгоритмы свящаны с блок-схемами?
# <p> Блок-схемы - это алгоритмы изображенные в графической форме.
#
# 1.5.3. Какую программу можно назвать хорошей?
# <p> Хорошая программа - программа с оптимальным алгоритмом. Так как она дает более быстрые результаты.
# Запишите все характеристики, какие удастся придумать.
# <p> Четкий, последовательный, максимально простой и короткий.
#
# 1.5.4. Какой язык понимает компьютер?
# Машинный.
#
# 1.5.5. Чем языки программирования отличаются от языков, на которых мы говорим?
# <p> В первую очередь они отличаются способом их интерпретации.
# Естественные языки, на которых мы говорим, интерпретируются нашим сознанием, порождая образы и дополняя нашу картину мира. Компьютерные языки преобразуются в машинный код, по средствам специальной программы, управляющий процессором и другими устройствами компьютера, которая сама по себе является порождением сознания человека.
# <p> Естественные языки намного сложнее и запутаннее, в них всегда есть исключения из правил и их интерпретация требует не просто  знания списка команд, как в случае с компьютерными языками, но и культурного контекста, в котором находится говорящий. Компьютерные язык являются формальными, практически без исключений.
# <p> Кроме информации они способны передавать эмоции, закладывать что то между строк. Одни и те же фразы, в зависимости от ситуации могут быть поняты совершенно по разному. В отличие от них языки программирования должны однозначно описывать алгоритм, состоящий из последовательности определенных действий и они, по сути, являются расширенной формой математических формул. Признаться в любви на них будет сложновато.

# 1.5.2. Правда или ложь.
# 1. Правда.
# 2. Ложь.
# 3. Ложь.
# 4. Правда.
# 5. Ложь.
# 6. Ложь.
# 7. Правда.
# 8. Ложь.
# 9. Правда.
# 10. Ложь.

# ## Практические задания.
# 1. Алгоритм расчета простых процентов от некоторой суммы.
# - шаг 1: Начало.
# - шаг 2: Присвойте переменной sum_ значение суммы.
# - шаг 3: Присвойте переменной percent размер процентов.
# - шаг 4: Введите формулу: sum_ / 100 * percent_
# - шаг 5: Напечатайте результат командой print
#
# 2. Алгоритм для вычисления площади прямоугольника.
# - шаг 1: Начало.
# - шаг 2: Присвойте переменной length значение длины прямоуголльника.
# - шаг 3: Присвойте переменной width значение ширины прямоугольника.
# - шаг 4: Введите формулу площади прямоугольника: the_area_of_the_rectangle = length * width
# - шаг 5: Напечатайте результат командой print
#
# 3. Алгоритм вычисления периметра круга.
# - шаг 1: Начало.
# - шаг 2: Присвойте переменной diameter значение диаметра круга.
# - шаг 3: Введите формулу периметра круга: the_perimeter_of_the_circle = diameter * pi
# - шаг 4: Напечатайте результат командой print.
#
# 4. Алгоритм, который находит все простые числа меньше 100.
# - шаг 1: Начало.
# -
#
# 5. Алгоритм превращения предложения, написанного в верхнем регистре, в обычный для предложений регистр.
# - шаг 1. Начало.
# - шаг 2. Применяем к str "HELLO WORLD!" метод capitalize.
# - шаг 3. Оборачиваем строку с методом в команду print.
#
# 1. Блок-схема приготовления льда из кипяченой воды с помощью холодильника.
#
# ![diagram1.png](attachment:diagram1.png)
#
# 2. Блок-схема для вычисления суммы всех четных чисел меньше ста.
#
#    ![diagram2.png](attachment:diagram2.png)
#
#
# 3. Блок-схема для вычисления квадрата всех нечетных чисел от 1 до 15 включительно.
#
#    ![diagram3.png](attachment:diagram3.png)
#
#
# 4.  Блок-схема вывода таблицы умножения на 3.
#
#    ![diagram4.png](attachment:diagram4.png)
#
# 5.  Блок-схема для расчета сложных процентов (с капитализацией).
#

sum_ = 100
percent = 10
resalt = sum_ / 100 * percent
resalt

sum_ = int(input())  # x.__int__()
percent = int(input())
resalt = sum_ / 100 * percent
resalt

length = 10
width = 5
the_area_of_the_rectangle = length * width
the_area_of_the_rectangle

diameter = 10
pi = 3.1415
the_perimeter_of_the_circle = diameter * pi
the_perimeter_of_the_circle

"HELLO, WORLD!".capitalize()

numbers = range(1, 100)
sum(num for num in numbers if not num % 2)

numbers = range(1, 16)
result = [num * num for num in numbers if num % 2 != 0]
result

numbers = range(1, 11)
result = [num * 3 for num in numbers]
result
