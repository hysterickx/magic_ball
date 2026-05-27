FRM_COLOR = '#0d0d0d'
TXT_COLOR_1 = '#99ff66'
TXT_COLOR_2 = '#ffffff'
TXT_COLOR_3 = '#ffff00'
BTN_COLOR_1 = '#99ff66'
BTN_COLOR_2 = '#ffffff'
BTN_COLOR_3 = '#000000'

BTN_PARAMS = {
    "height": 50,
    "corner_radius": 50,
    "fg_color": BTN_COLOR_1,
    "hover_color": BTN_COLOR_2,
    "text_color": BTN_COLOR_3,
    "font": ('Constantia', 20)
}

MSG_PARAMS = {
    "width": 300,
    "height": 150,
    "title": 'Ошибочка',
    "icon": 'info',
    "justify": 'center',
    "button_color": BTN_COLOR_2,
    "button_hover_color": BTN_COLOR_1,
    "button_text_color": BTN_COLOR_3
}

ENTRY_PARAMS = {
    "width": 500,
    "height": 30,
    "corner_radius": 40,
    "justify": 'c',
    "text_color": TXT_COLOR_1,
    "font": ('Cambria', 27)
}

BALL_PARAMS = {
    "text": '',
    "width": 200,
    "height": 200,
    "corner_radius": 100,
    "fg_color": 'red',
    "hover_color": 'red',
}

ERROR_MESSAGES = {
    'empty': 'В поле пусто',
    'too_short': 'Слишком мало символов',
    'not_alpha': 'А как же буковки?',
    'not_question': 'Шару нужен знак вопроса в конце'
}

GAME_MESSAGES = {
    'answers': [
        'Бесспорно', 'Предрешено', 'Никаких сомнений',
        'Определённо да', 'Можешь быть уверен в этом',
        'Мне кажется - да', 'Вероятнее всего',
        'Хорошие перспективы', 'Знаки говорят - да', 'Да',
        'Пока неясно, попробуй снова', 'Спроси позже',
        'Лучше не рассказывать', 'Сейчас нельзя предсказать',
        'Сконцентрируйся и спроси опять', 'Даже не думай',
        'Мой ответ - нет', 'По моим данным - нет',
        'Перспективы не очень хорошие', 'Весьма сомнительно'
    ],
    'waiting_words': [
        'Жду ответа от Вселенной...', 'Посылаю запрос в космос...',
        'Звёзды просят немного подождать...', 'Дай-ка подумать...',
        'Получаю твой ответ...'
    ],
    'loading_words': [
        'Генерирую цикл...',
        'Создаю всё с нуля...',
        'Очищаю всё лишнее...',
        'Отлично! Начинаем...',
        'Дай мне пару секундочек!'
    ],
    'farewell_words': [
        'До новых встреч!',
        'Заглядывай ко мне ещё!',
        'Был рад поработать с тобой!',
        'Ты это, заходи, если что...',
        'Надеюсь, еще увидимся!'
    ]
}

COLORS = [
    '#99ff66', '#ff1493', '#00ffff', '#ffe119', '#3cb44b', '#f58231', '#f032e6', '#bcf60c',
    '#fabebe', '#e6beff', '#fffac8', '#aaffc3', '#ffd8b1', '#ff00ff', '#00ff7f', '#1e90ff',
    '#ff8c00', '#ba55d3', '#adff2f', '#ff6347', '#40e0d0', '#7b68ee', '#00fa9a', '#ff4500',
    '#12cbc4', '#fda7df', '#ed4c67', '#a3cb38', '#2ed573', '#ff4757', '#ffa502', '#7efff5',
    '#fffa65', '#ffaf40', '#ff1e56', '#ffacb7', '#baffc9', '#ffb3ff', '#85e3ff', '#9797ff',
    '#e1ffb1', '#ffd3b6', '#ff8b94', '#ffaaa5', '#a8e6cf', '#dcedc1', '#ffd3b6', '#ff8b94',
    '#00ffcc', '#ccff00'
]