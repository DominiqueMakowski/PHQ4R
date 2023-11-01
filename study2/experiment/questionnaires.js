// Depression-Anxiety (Patient Health Questionnaire-4, PHQ-4)
var PHQ4_instructions =
    "<p><b>About your emotions...</b></p>" +
    "<p>Over the <b>last 2 weeks</b>, how often have you been bothered by the following problems?</p>"

var PHQ4_items = [
    "Feeling nervous, anxious or on edge",
    "Not being able to stop or control worrying",
    "Feeling down, depressed, or hopeless",
    "Little interest or pleasure in doing things",
]

var PHQ4_dimensions = ["Anxiety_1", "Anxiety_2", "Depression_3", "Depression_4"]

// Questionnaire ========================================================================

function phq4() {
    condition = jsPsych.randomization.sampleWithoutReplacement(
        ["PHQ4", "PHQ4R"],
        1
    )[0]

    if (condition == "PHQ4") {
        labels = [
            "<br>Not at all",
            "<br>Several days",
            "<br>More than half the days",
            "<br>Nearly every day",
        ]
    } else if (condition == "PHQ4R") {
        labels = [
            "<br>Not at all",
            "<br>Once or twice", // New option
            "<br>Several days",
            "<br>More than half the days",
            "<br>Nearly every day",
        ]
    }

    PHQ4_questions = []
    for (const [index, element] of PHQ4_items.entries()) {
        PHQ4_questions.push({
            prompt: "<b>" + element + "</b>",
            name: PHQ4_dimensions[index],
            labels: labels,
            required: true,
        })
    }

    return {
        type: jsPsychSurveyLikert,
        questions: PHQ4_questions,
        randomize_question_order: false,
        preamble: PHQ4_instructions,
        data: {
            screen: "questionnaire_phq4",
            condition: condition,
        },
    }
}

// BDI-II ========================================================================
var bdi2 = {
    type: jsPsychSurveyMultiChoice,
    preamble:
        "<p style='width:50%; margin-left: auto; margin-right: auto' align='center'>This questionnaire consists of 21 groups of statements. Please read each group of statements carefully. And then pick out the one statement in each group that best describes the way you have been feeling during the past two weeks, including today. If several statements in the group seem to apply equally well, circle the highest number for that group.</p>",
    questions: [
        {
            prompt: "<b>1. Sadness</b>",
            options: [
                "0. I do not feel sad",
                "1. I feel sad much of the time",
                "2. I am sad all the time",
                "3. I am so sad or unhappy that I can't stand it",
            ],
            name: "bdi2_1",
        },
    ],
    data: {
        screen: "questionnaire_bdi2",
    },
}
