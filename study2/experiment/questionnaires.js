// Mini IPIP6 questionnaire
var ipip6_items = [
    // I am the life of the party
    "Я - душа любой вечеринки",
    // I sympathise with others' feelings
    "Я сопереживаю эмоциям других людей",
    // I get chores done right away
    "Я сразу выполняю домашние дела",
    // I have frequent mood swings
    "Мое настроение часто меняется",
    // I have a vivid imagination
    "У меня богатое воображение",
    // I feel entitled to more of everything
    "Я считаю, что мне должно доставаться больше, чем то, что я получаю сейчас",
    // I don't talk a lot
    "Я не многословен/многословна",
    // I am not interested in other people's problems
    "Мне не интересны проблемы других людей",
    // I have difficulty understanding abstract ideas
    "Мне трудно понимать абстрактные идеи",
    // I like order
    "Я люблю порядок",
    // I make a mess of things
    "Я устраиваю беспорядок",
    // I deserve more things in life
    "Я заслуживаю большего в жизни",
    // I do not have a good imagination
    "У меня не очень хорошее воображение",
    // I feel others' emotions
    "Я чувствую эмоции других людей",
    // I am relaxed most of the time
    "Большую часть времени я расслаблен",
    // I get upset easily
    "Меня легко расстроить",
    // I seldom feel blue
    "Я редко чувствую себя грустным(ой)",
    // I would like to be seen driving around in a really expensive car
    "Я бы хотел(а), что бы меня видели за рулем очень дорогой машины",
    // I keep in the background
    "Я стараюсь оставаться в тени",
    // I am not really interested in others
    "Меня не очень интересуют другие люди",
    // I am not interested in abstract ideas
    "Меня не интересуют абстрактные идеи",
    // I often forget to put things back in their proper place
    "Я часто забываю положить вещи на место",
    // I talk to a lot of different people at parties
    "На вечеринках я общаюсь с большим количеством разных людей",
    // I would get a lot of pleasure from owning expensive luxury goods
    "Я получил(а) бы много удовольствия от владения дорогими предметами роскоши",
]
var ipip6_dimensions = [
    "Extraversion_1",
    "Agreeableness_2",
    "Conscientiousness_3",
    "Neuroticism_4",
    "Openness_5",
    "HonestyHumility_6_R",
    "Extraversion_7_R",
    "Agreeableness_8_R",
    "Openness_9_R",
    "Conscientiousness_10",
    "Conscientiousness_11_R",
    "HonestyHumility_12_R",
    "Openness_13_R",
    "Agreeableness_14",
    "Neuroticism_15_R",
    "Neuroticism_16",
    "Neuroticism_17_R",
    "HonestyHumility_18_R",
    "Extraversion_19_R",
    "Agreeableness_20_R",
    "Openness_21_R",
    "Conscientiousness_22_R",
    "Extraversion_23",
    "HonestyHumility_24_R",
]

// Personality Inventory for DSM-V - Brief (Maladaptive Traits)
var pid_items = [
    // People would describe me as reckless
    "По мнению людей, я безрассудный человек",
    // I feel like I act totally on impulse
    "Мне кажется, я действую только под влиянием импульса",
    // Even though I know better, I can't stop making rash decisions
    "Я понимаю, что это неверно, но все равно принимаю опрометчивые решения",
    // I often feel like nothing I do really matters
    "Я часто ощущаю, что мои действия не имеют значения",
    // Others see me as irresponsible
    "Другие видят меня безответственным человеком",
    // I'm not good at planning ahead
    "Я не умею планировать наперед",
    // My thoughts often don't make sense to others
    "Мои мысли часто непонятны другим",
    // I worry about almost everything
    "Я беспокоюсь практически из-за всего",
    // I get emotional easily, often for very little reason
    "Я легко расстраиваюсь, часто почти без причины",
    // I fear being alone in life more than anything else
    "Больше всего я боюсь остаться один",
    // I get stuck on one way of doing things, even when it's clear it won't work
    "Я зацикливаюсь на одном варианте, даже если очевидно, что он не работает",
    // I have seen things that weren't really there
    "Я видел вещи, которых на самом деле не было",
    // I steer clear of romantic relationships
    "Я сторонюсь романтических отношений",
    // I'm not interested in making friends
    "Меня не интересует дружба",
    // I get irritated easily by all sorts of things
    "Меня легко приводят в раздражение самые разнообразные вещи",
    // I don't like to get too close to people
    "Мне не нравится сближаться с людьми",
    // It's no big deal if I hurt other people's feelings
    "Ничего страшного не случится, если я задену чувства другого человека",
    // I rarely get enthusiastic about anything
    "Я редко испытываю воодушевление по какому-либо поводу",
    // I crave attention
    "Я жажду внимания",
    // I often have to deal with people who are less important than me
    "Мне часто приходится иметь дело с людьми, которые менее значительны, чем я",
    // I often have thoughts that make sense to me but that other people say are strange
    "Меня часто посещают мысли, которые кажутся мне вполне разумными, но другим они кажутся странными",
    // I use people to get what I want
    "Я пользуюсь людьми, чтобы получить то, чего хочу",
    // I often 'zone out' and then suddenly come to and realise that a lot of time has passed
    "Я часто «отключаюсь» и потом внезапно прихожу в сознание и понимаю, что прошло уже много времени",
    // Things around me often feel unreal, or more real than usual
    "Все вокруг часто кажется мне нереальным или, наоборот, реальнее, чем обычно",
    // It is easy for me to take advantage of others
    "Я легко пользуюсь другими в своих интересах",
]

var pid_dimensions = [
    "Disinhibition_1",
    "Disinhibition_2",
    "Disinhibition_3",
    "Detachment_4",
    "Disinhibition_5",
    "Disinhibition_6",
    "Psychoticism_7",
    "NegativeAffect_8",
    "NegativeAffect_9",
    "NegativeAffect_10",
    "NegativeAffect_11",
    "Psychoticism_12",
    "Detachment_13",
    "Detachment_14",
    "NegativeAffect_15",
    "Detachment_16",
    "Antagonism_17",
    "Detachment_18",
    "Antagonism_19",
    "Antagonism_20",
    "Psychoticism_21",
    "Antagonism_22",
    "Psychoticism_23",
    "Psychoticism_24",
    "Antagonism_25",
]

// Short Suggestibility Scale (SSS  21 items; Kotov, Bellman & Watson, 2004)
// From the Multidimensional Iowa Suggestibility Scale (MISS)
var sss_items = [
    "I am easily influenced by other people's opinions",
    "I can be influenced by a good commercial",
    "When someone coughs or sneezes, I usually feel the urge to do the same",
    "Imagining a refreshing drink can make me thirsty",
    "A good salesperson can really make me want their product",
    "I get a lot of good practical advice from magazines or TV",
    "If a product is nicely displayed, I usually want to buy it",
    "When I see someone shiver, I often feel a chill myself",
    "I get my style from certain celebrities",
    "When people tell me how they feel, I often notice that I feel the same way",
    "When making a decision, I often follow other people's advice",
    "Reading descriptions of tasty dishes can make my mouth water",
    "I get many good ideas from others",
    "I frequently change my opinion after talking with others",
    "After I see a commercial for lotion, sometimes my skin feels dry",
    "I discovered many of my favorite things through my friends",
    "I follow current fashion trends",
    "Thinking about something scary can make my heart pound",
    "I have picked-up many habits from my friends",
    "If I am told I don't look well, I start feeling ill",
    "It is important for me to fit in",
]

var sss_dimensions = [
    "SSS_1",
    "SSS_2",
    "SSS_3",
    "SSS_4",
    "SSS_5",
    "SSS_6",
    "SSS_7",
    "SSS_8",
    "SSS_9",
    "SSS_10",
    "SSS_11",
    "SSS_12",
    "SSS_13",
    "SSS_14",
    "SSS_15",
    "SSS_16",
    "SSS_17",
    "SSS_18",
    "SSS_19",
    "SSS_20",
    "SSS_21",
]

// Questionnaire ========================================================================

// Functions
function format_questions_analog(
    items,
    dimensions,
    // Response options in English "Inaccurate", "Accurate"
    ticks = ["Неверно", "Верно"]
) {
    var questions = []
    for (const [index, element] of items.entries()) {
        questions.push({
            prompt: "<b>" + element + "</b>",
            name: dimensions[index],
            ticks: ticks,
            required: false,
            min: 0,
            max: 1,
            step: 0.01,
            slider_start: 0.5,
        })
    }
    return questions
}

// IPIP
var ipip6_questionaire = {
    type: jsPsychMultipleSlider,
    // This function is loaded in RestingState.js
    questions: format_questions_analog(ipip6_items, ipip6_dimensions),
    randomize_question_order: false,
    preamble:
        // About your personality... Please answer the following questions based on how accurately each statement describes you in general.
        "<p>Пожалуйста, ответите на следующие вопросы исходя из того, насколько точно каждое утверждение описывает Вас в целом.</p>",
    require_movement: false,
    slider_width: 600,
    data: {
        screen: "IPIP6",
    },
}

// PID
var pid_questions = []
for (const [index, element] of pid_items.entries()) {
    pid_questions.push({
        prompt: "<b>" + element + "</b>",
        name: pid_dimensions[index],
        labels: [
            // Very or Often False
            "Совершенно неверно или часто неверно",
            // Sometimes or Somewhat False
            "Иногда или в некоторой степени неверно",
            // Sometimes or Somewhat True
            "Иногда или в некоторой степени верно",
            // Very or Often True
            "Совершенно верно или часто верно",
        ],
        required: false,
    })
}

var pid5_questionaire = {
    type: jsPsychSurveyLikert,
    questions: pid_questions,
    randomize_question_order: false,
    preamble:
        // About yourself... Below is a list of things different people might say about themselves. Please select the response that best describes you.
        "<p>Перед Вами список утверждений, которые разные люди могут использовать для того, чтобы охарактеризовать себя.</p>" +
        "<p>Пожалуйста, выберите ответ, который наилучшим образом описывает Вас.</p>",
    button_label: "Продолжить",
    require_movement: false,
    slider_width: 700,
    data: {
        screen: "PID5",
    },
}

// SSS
var sss_questions = []
for (const [index, element] of sss_items.entries()) {
    sss_questions.push({
        prompt: "<b>" + element + "</b>",
        name: sss_dimensions[index],
        labels: [
            "Not at all or very slightly",
            "A little",
            "Somewhat",
            "Quite a bit",
            "A lot",
        ],
        required: false,
    })
}

var sss_questionaire = {
    type: jsPsychSurveyLikert,
    questions: sss_questions,
    randomize_question_order: true,
    preamble:
        "<p><b>About your sensitivity and adaptability...</b></p>" +
        "<p>Please indicate to what extent the following statements apply to you.</p>",
    button_label: "Продолжить",
    require_movement: false,
    slider_width: 700,
    data: {
        screen: "SSS",
    },
}
