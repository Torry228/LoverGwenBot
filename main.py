import telebot, random



from config import bot


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['all'])
def main(message):
    bot.send_message(message.chat.id,'@LoverGwen, @nathanest, @Kristov37, @Riwek, @salen25, @Ml4AU22, @ImWombat, @Its_TIMMMYYY')

@bot.message_handler(commands=['lolgay'])
def main(message):
    bot.send_message(message.chat.id,'@LoverGwen, @nathanest, @Kristov37, @Riwek, @salen25, @Ml4AU22')

@bot.message_handler(commands=['deadinside'])
def main(message):
    bot.send_message(message.chat.id,'@Its_TIMMMYYY')

@bot.message_handler(commands=['backvkonavu'])
def main(message):
    bot.send_message(message.chat.id,'@ImWombat')

@bot.message_handler(commands=['alinaobed'])
def main(message):
    bot.send_message(message.chat.id,'К Алиночке Рамилевне на обед можно? @LoverGwen, @nathanest, @Kristov37, @Riwek')

@bot.message_handler(commands=['alinano'])
def main(message):
        bot.send_message(message.chat.id, 'К Алиночке Рамилевне на обед нельзя! @LoverGwen, @nathanest, @Kristov37, @Riwek')

@bot.message_handler(commands=['alinayes'])
def main(message):
        bot.send_message(message.chat.id, 'К Алиночке Рамилевне на обед можно, пошлите тусить! @LoverGwen, @nathanest, @Kristov37, @Riwek')

@bot.message_handler(commands=['kill'])
def main(message):
        bot.send_message(message.chat.id, f'Ты думал, это майнкрафт, @{message.from_user.username}?')

@bot.message_handler(commands=['tp'])
def main(message):
        bot.send_message(message.chat.id, 'Мое тп отменено, катка проиграна давно')



@bot.message_handler(commands=['bad'])
def main(message):
        bot.send_message(message.chat.id, 'Гвеночка невосприимчивая')



messages = [
    'Беги, и получишь копьё в спину.',
    'Я призываю звёзды испечь для меня пышный хлеб!',
    'Атрокс, Губитель пива! Ты знаешь, что смерть порождает жизнь?',
    'Спину прямо, ножницы держим ровненько!',
    'Чик-чик!',
    'Всех пришью!',
    'Куда-то идёшь?',
    'Мой дом – мои правила.',
    'Я? Безумен? Пожалуй.',
    'Рев Рек`Сай',
    'Ты же хочешь меня?',
    'Ты не первый мой дракон.',
    'Да, детка, раскрепостись.',
    'Умная лисица никогда не попадётся.',
    'Вместе всегда веселее. Правда?',
    'Хвостов у меня девять, а жизней… неограниченное количество.',
    'Капитан Тимо на посту!',
    'Так точно!',
    'Размер не имеет значения!',
    'Я прекрасен в бою, как цветок на рассвете.',
    'Мои критики долго не живут.',
    'Я живу ради оваций, а ты ради них умрёшь.',
    'Льётся кровь, враги бегут.',
    'Овца… на убой.',
    'Мясо!',
    'Вместе мы справимся!',
    'Рыбка-рыбка! Ааа!',
    'Туда! Нет, туда! Ах, ну ладно, туда…',
    'Поехали.',
    'Сила есть — ума не надо.',
    'Попробуй увернуться!',
    'На моих крыльях.',
    'Я несу бурю.',
    'Я – снег, ветер, и лёд.',
    'Убийца без хозяина опасен вдвойне.',
    'Я могу сделать это быстро, а могу очень быстро. Выбирай.',
    'Идеальное убийство.',
    'Внемли безмолвию смерти.',
    'Я – ГИБЕЛЬ!',
    'Я – АТРОКС! Я – ГУБИТЕЛЬ ПИВА!',
    'ЧОтыре!!!!',
    'Судьба. Власть. Коварство. Секс. Наркотики. Голые сиськи',
    'Welcome To Brazil',
    'Я снова воплощён в металле.',
    'Прощай, Каин! Да начнётся бойня!',
    'Я – воплощение смерти!',
    'Покажи, чего ты стоишь! Сам разбирайся.',
    'Какое чудовище может убить ребёнка? А, ну да…',
    'Я психованная! У меня справка есть!',
    'Люблю ломать стереотипы… А ещё здания. И людей!',
    'Вера – самое грозное оружие из твоего арсенала, Афелий.',
    'Калибрум!',
    'Северум.',
    'Гравитум.',
    'Инфернум!',
    'Кресцендум!',
    'Художник должен знать свою модель.',
    'Хорошо тебе. Никаких забот, никаких сроков.',
    'Стань моим холстом!',
    'Мы не будем носить намордники',
    'Кто хороший пёсик?… Мы.',
    'Стая растет!',
    'Мои сердце и меч принадлежат Демасии.',
    'ДЕМАСИЯ!!!',
    'За Демасию!',
    'Приятно познакомиться, я голодна… то есть, Брайер!',
    'Ааа… Это называется "стратегия", да?',
    'Ээээ… как мне тебя называть? Владимир? Или папа?..',
    'Нико – это лучший выбор!',
    'Нико нельзя приручить.',
    'Нет, хвост! Сейчас мы злимся!',
    'Я беру это дело.',
    'Ха. Может ещё жетон с винтовкой сдать?',
    'Беру на прицел.',
    'Жизнь слишком коротка, чтобы бояться.',
    'Всех на дно.',
    'Теперь ты в моём списке.',
    'Вот твоя доля.',
    'Начнём охоту на тех, кто продался тьме.',
    'Трепещите перед совершенством.',
    'Фортуна не покровительствует дуракам.',
    'Думаешь, можешь мною управлять, призыватель?',
    'Звериный отряд, к бою!',
]

@bot.message_handler(commands=['random_replicas'])
def send_random_message(message):
    random_message = random.choice(messages)
    bot.send_message(message.chat.id, random_message)


bot.polling(none_stop=True)


