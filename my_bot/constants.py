# THREAD_ID = {
#     "Безопасность": 44,
#     "Маркетинг, Реклама, PR": 57,
#     "IT": 56,
#     "Продажи, Обслуживание клиентов": 54,
#     "Юристы": 107,
#     "Административный персонал": 43,
#     "Курьеры": 7,
#     "Управление персоналом": 10,
#     "Финансы, Бухгалтерия": 4,
#     "Розничная торговля": 5
# }

THREAD_KEYWORDS = {
    44: [
        'безопасность',
        'охрана',
        'видеонаблюдение',
        'системы контроля доступа',
        'противопожарная защита'
    ],
    57: [
        "маркетинг",
        "реклама",
        "pr",
        "стратегия маркетинга",
        "цифровой маркетинг",
        "интернет-маркетинг",
        "брендинг"
    ],
    56: [
        'разработка',
        'разработчик',
        'разработка ПО',
        'аналитика данных',
        'информационная безопасность',
        'IT-консалтинг',
        'системный администратор',
        'базы данных'
    ],
    54: [
        'продажи',
        'обслуживание клиентов',
        'активные продажи',
        'клиентский сервис',
        'торговые навыки'
    ],
    107: [
        'юристы',
        'законодательство',
        'правовая помощь',
        'судебные споры',
        'корпоративное право',
        'гражданское право',
        'интеллектуальная собственность'
    ],
    43: [
        'административный персонал',
        'секретариат',
        'офисный персонал',
        'организация мероприятий',
        'офисное управление',
        'администрирование баз данных',
        'планирование рабочего времени'
    ],
    7: [
        'курьеры',
        'доставка',
        'логистика',
        'экспресс-доставка',
        'маршрутное планирование',
        'грузоперевозки',
        'складское хозяйство'
    ],
    10: [
        'управление персоналом',
        'HR',
        'кадровое делопроизводство',
        'развитие персонала',
        'трудовое законодательство',
        'конфликтология',
        'мотивация сотрудников'
    ],
    4: [
        'финансы',
        'бухгалтерия',
        'финансовый анализ',
        'налоговое планирование',
        'аудит',
        'бухгалтерское обслуживание',
        'финансовое планирование'
    ],
    5: [
        'розничная торговля',
        'управление магазином',
        'продажи',
        'инвентаризация',
        'торговое оборудование',
        'покупательская аналитика',
        'маркетинговые акции'
    ]
}

RULES_TEXT = ('''
    ПРАВИЛА ПУБЛИКАЦИИ ВАКАНСИЙ:
    
    ▪️Вакансии размещаются БЕСПЛАТНО. 
            
    ▪️Повторная публикация возможна через 30 минут.
    
    ▪️Резюме и бартерные вакансии НЕ размещаем.
        
    ▪️При большом отклике по вашей просьбе вакансию удаляем. 
        
    ▪️Принимаются к размещению только КОРРЕКТНО ЗАПОЛНЕННЫЕ заявки.
    
    ''')

EXAMPLE = ('''
Шаблон оформления заявки:

❗️Просим не добавлять свои эмодзи/другую информацию, не убирать блоки, и не применять выделения/подчеркивания.

(Иначе ваше сообщение попросту не поубликуется)

#Блок#Из#Минимум#Пяти#Хэштегов

Название фирмы | указать город (если необходимо)
    
Должность:
- … 
- …
- …

Требования к кандидату: 
- … 
- …
- …

Условия работы: 
- … 
- …
- …
ЗП/Оклад:
- … 
- …
- …    

Контактные данные: (ссылка на Telegram/номер телефона/почта/ссылка на Google Форму).

Копируйте и заполняйте.
''')