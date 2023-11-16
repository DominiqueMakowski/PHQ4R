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

// STAIT-5 (Zsido, 2020) ========================================================================
var stai5_items = [
    "I feel that difficulties are piling up so that I cannot overcome them",
    "I worry too much over something that really doesn't matter",
    "Some unimportant thoughts run through my mind and bothers me",
    "I take disappointments so keenly that I can't put them out of my mind",
    "I get in a state of tension or turmoil as I think over my recent concerns and interests",
]

var stai5_dimensions = ["stai5_1", "stai5_2", "stai5_3", "stai5_4", "stai5_5"]

stai5_questions = []
for (const [index, element] of stai5_items.entries()) {
    stai5_questions.push({
        prompt: "<b>" + element + "</b>",
        name: stai5_dimensions[index],
        labels: [
            "<br>Not at all",
            "<br>Somewhat",
            "<br>Moderately so",
            "<br>Very much so",
        ],
        required: true,
    })
}

var stai5 = {
    type: jsPsychSurveyLikert,
    css_classes: ["multichoice-narrow"],
    questions: stai5_questions,
    randomize_question_order: false,
    preamble:
        "<p style='text-align: left;'>A number of statements which people have used to describe themselves are given below. Read each statement and then circle the number at the end of the statement that indicates " +
        // "HOW YOU FEEL RIGHT NOW. " +
        "how you have been feeling <b>during the past two weeks</b>. " +
        "There are no right or wrong answers. Do not spend too much time on any one statement but give the answer which seems to describe your present feelings best.</p> ",
    data: {
        screen: "questionnaire_stai5",
    },
}

// BDI-II ========================================================================
var bdi2 = {
    type: jsPsychSurveyMultiChoice,
    css_classes: ["multichoice-narrow"],
    preamble:
        "<p style='text-align: left;'>This questionnaire consists of 21 groups of statements. Please read each group of statements carefully. And then pick out the one statement in each group that best describes the way you have been feeling <b>during the past two weeks</b>, including today. If several statements in the group seem to apply equally well, circle the highest number for that group.</p>",
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
        {
            prompt: "<b>2. Pessimism</b>",
            options: [
                "0. I am not discouraged about my future",
                "1. I feel more discouraged about my future than I used to",
                "2. I do not expect things to work out for me",
                "3. I feel my future is hopeless and will only get worse",
            ],
            name: "bdi2_2",
        },
        {
            prompt: "<b>3. Past Failure</b>",
            options: [
                "0. I do not feel like a failure",
                "1. I have failed more than I should have",
                "2. As I look back, I see a lot of failures",
                "3. I feel I am a total failure as a person",
            ],
            name: "bdi2_3",
        },
        {
            prompt: "<b>4. Loss of Pleasure</b>",
            options: [
                "0. I get as much pleasure as I ever did from the things I enjoy",
                "1. I don't enjoy things as much as I used to",
                "2. I get very little pleasure from the things I used to enjoy",
                "3. I can't get any pleasure from the things I used to enjoy",
            ],
            name: "bdi2_4",
        },
        {
            prompt: "<b>5. Guilty Feelings</b>",
            options: [
                "0. I don't feel particularly guilty",
                "1. I feel guilty over many things I have done or should have done",
                "2. I feel quite guilty most of the time",
                "3. I feel guilty all of the time",
            ],
            name: "bdi2_5",
        },
        {
            prompt: "<b>6. Punishment Feelings</b>",
            options: [
                "0. I don't feel I am being punished",
                "1. I feel I may be punished",
                "2. I expect to be punished",
                "3. I feel I am being punished",
            ],
            name: "bdi2_6",
        },
        {
            prompt: "<b>7. Self-Dislike</b>",
            options: [
                "0. I feel the same about myself as ever",
                "1. I have lost confidence in myself",
                "2. I am disappointed in myself",
                "3. I dislike myself",
            ],
            name: "bdi2_7",
        },
        {
            prompt: "<b>8. Self-Criticalness</b>",
            options: [
                "0. I don't criticize or blame myself more than usual",
                "1. I am more critical of myself than I used to be",
                "2. I criticize myself for all of my faults",
                "3. I blame myself for everything bad that happens",
            ],
            name: "bdi2_8",
        },
        {
            prompt: "<b>9. Suicidal Thoughts or Wishes</b>",
            options: [
                "0. I don't have any thoughts of killing myself",
                "1. I have thoughts of killing myself, but I would not carry them out",
                "2. I would like to kill myself",
                "3. I would kill myself if I had the chance",
            ],
            name: "bdi2_9",
        },
        {
            prompt: "<b>10. Crying</b>",
            options: [
                "0. I don't cry anymore than I used to",
                "1. I cry more than I used to",
                "2. I cry over every little thing",
                "3. I feel like crying, but I can't",
            ],
            name: "bdi2_10",
        },
        {
            prompt: "<b>11. Agitation</b>",
            options: [
                "0. I am no more restless or wound up than usual",
                "1. I feel more restless or wound up than usual",
                "2. I am so restless or agitated, it's hard to stay still",
                "3. I am so restless or agitated that I have to keep moving or doing something",
            ],
            name: "bdi2_11",
        },
        {
            prompt: "<b>12. Loss of Interest</b>",
            options: [
                "0. I have not lost interest in other people or activities",
                "1. I am less interested in other people or things than before",
                "2. I have lost most of my interest in other people or things",
                "3. It's hard to get interested in anything",
            ],
            name: "bdi2_12",
        },
        {
            prompt: "<b>13. Indecisiveness</b>",
            options: [
                "0. I make decisions about as well as ever",
                "1. I find it more difficult to make decisions than usual",
                "2. I have much greater difficulty in making decisions than I used to",
                "3. I have trouble making any decisions",
            ],
            name: "bdi2_13",
        },
        {
            prompt: "<b>14. Worthlessness</b>",
            options: [
                "0. I do not feel I am worthless",
                "1. I don't consider myself as worthwhile and useful as I used to",
                "2. I feel more worthless as compared to others",
                "3. I feel utterly worthless",
            ],
            name: "bdi2_14",
        },
        {
            prompt: "<b>15. Loss of Energy</b>",
            options: [
                "0. I have as much energy as ever",
                "1. I have less energy than I used to have",
                "2. I don't have enough energy to do very much",
                "3. I don't have enough energy to do anything",
            ],
            name: "bdi2_15",
        },
        {
            prompt: "<b>16. Changes in Sleeping Pattern</b>",
            options: [
                "0. I have not experienced any change in my sleeping pattern",
                "1a. I sleep somewhat more than usual",
                "1b. I sleep somewhat less than usual",
                "2a. I sleep a lot more than usual",
                "2b. I sleep a lot less than usual",
                "3a. I sleep most of the day",
                "3b. I wake up 1-2 hours early and can't get back to sleep",
            ],
            name: "bdi2_16",
        },
        {
            prompt: "<b>17. Irritability</b>",
            options: [
                "0. I am not more irritable than usual",
                "1. I am more irritable than usual",
                "2. I am much more irritable than usual",
                "3. I am irritable all the time",
            ],
            name: "bdi2_17",
        },
        {
            prompt: "<b>18. Changes in Appetite</b>",
            options: [
                "0. I have not experienced any change in my appetite",
                "1a. My appetite is somewhat less than usual",
                "1b. My appetite is somewhat greater than usual",
                "2a. My appetite is much less than before",
                "2b. My appetite is much greater than usual",
                "3a. I have no appetite at all",
                "3b. I crave food all the time",
            ],
            name: "bdi2_18",
        },
        {
            prompt: "<b>19. Concentration Difficulty</b>",
            options: [
                "0. I can concentrate as well as ever",
                "1. I can't concentrate as well as usual",
                "2. It's hard to keep my mind on anything for very long",
                "3. I find I can't concentrate on anything",
            ],
            name: "bdi2_19",
        },
        {
            prompt: "<b>20. Tiredness or Fatigue</b>",
            options: [
                "0. I am no more tired or fatigued than usual",
                "1. I get more tired or fatigued more easily than usual",
                "2. I am too tired or fatigued to do a lot of the things I used to do",
                "3. I am too tired or fatigued to do most of the things I used to do",
            ],
            name: "bdi2_20",
        },
        {
            prompt: "<b>21. Loss of Interest in Sex</b>",
            options: [
                "0. I have not noticed any recent change in my interest in sex",
                "1. I am less interested in sex than I used to be",
                "2. I am much less interested in sex now",
                "3. I have lost interest in sex completely",
            ],
            name: "bdi2_21",
        },
    ],
    data: {
        screen: "questionnaire_bdi2",
    },
}
