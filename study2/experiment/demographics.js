// Retrieve and save browser info ========================================================
var demographics_browser_info = {
    type: jsPsychBrowserCheck,
    data: {
        screen: "browser_info",
        date: new Date().toLocaleDateString("fr-FR"),
        time: new Date().toLocaleTimeString("fr-FR"),
    },
    on_finish: function () {
        data = jsPsych.data.get().filter({ screen: "browser_info" }).values()[0]
        jsPsych.data.addProperties({
            ["screen_height"]: data["height"],
            ["screen_width"]: data["width"],
        })
        for (var key in data) {
            if (
                [
                    "vsync_rate",
                    "os",
                    "mobile",
                    "browser",
                    "browser_version",
                ].includes(key)
            ) {
                jsPsych.data.addProperties({
                    [key]: data[key],
                })
            }
        }
        jsPsych.data.addProperties()
    },
}

// Participant ID ========================================================================
var demographics_participant_id = {
    type: jsPsychSurveyText,
    questions: [
        {
            prompt: "Enter participant ID:",
            placeholder: "001",
            name: "Participant_ID",
        },
    ],
    data: {
        screen: "participant_id",
    },
    on_finish: function () {
        // Store `participant_id` so that it can be reused later
        jsPsych.data.addProperties({
            participant_id: jsPsych.data.get().last().values()[0]["response"][
                "Participant_ID"
            ],
        })
    },
}

// Consent form ========================================================================
var demographics_consent = {
    type: jsPsychHtmlButtonResponse,
    stimulus:
        // Logo
        "<img src='https://blogs.brighton.ac.uk/sussexwrites/files/2019/06/University-of-Sussex-logo-transparent.png' width='150px' align='right'/><br><br><br><br><br>" +
        // Title
        "<h1>Informed Consent</h1>" +
        "<p align='left'>Thank you for considering participating in our research. This study contains various questionnaires about your personality, feelings and current state of mind.</p>" +
        "<p>The aim is for us to understand how <b>mood fluctuations</b> and mood disorders symptoms (or absence thereof) are expressed and what difficulties they can generate.</p>" +
        "<p align='left'>Your participation in this research will be kept completely confidential. Your responses are entirely anonymous, and no IP address or any identifiers is collected.</p>" +
        "<p align='left'><b>By participating, you agree to follow the instructions and provide honest answers.</b> If you do not wish to participate this survey, simply close your browser.</p>" +
        // "<p>Please note that various checks will be performed to ensure the validity of the data.<br>We reserve the right to return your participation or prorate reimbursement should we detect non-valid responses (e.g., random pattern of answers, instructions not read, ...).</p>"

        "<p align='left'><br><sub><sup>If you have any questions about the project, please contact D.Makowski@sussex.ac.uk. This project has been reviewed and approved by the Ethics Comitee of the University of Sussex (TODO).</sup></sub></p>",

    choices: ["I consent"],
    data: { screen: "consent" },
}

// Thank you ========================================================================
var demographics_endscreen = {
    type: jsPsychHtmlButtonResponse,
    css_classes: ["multichoice-narrow"],
    stimulus:
        "<h1>Thank you for participating</h1>" +
        "<p>It means a lot to us. Don't hesitate to share the study!</p>" +
        "<p align='left'>The purpose of this study was for us to understand how mood fluctuations and mood disorder symptoms (or absence thereof) are expressed and what difficulties they can generate. Your participation in this study will be kept completely confidential.</p>" +
        "<p>Click on 'Continue' and <b>wait until your responses have been successfully saved</b> before closing the tab.</p> ",
    choices: ["Continue"],
    data: { screen: "endscreen" },
}

// Demographic info ========================================================================
var demographics_multichoice = {
    type: jsPsychSurveyMultiChoice,
    preamble: "<b>Please answer the following questions:</b>",
    questions: [
        {
            prompt: "What is your gender?",
            options: ["Male", "Female", "Other"],
            name: "gender",
        },
        // {
        //     prompt: "Are you currently a student?",
        //     options: ["Yes", "No"],
        //     name: "student",
        // },
        {
            prompt: "What is your highest completed education level?",
            options: [
                "University (doctorate)",
                "University (master) <sub><sup>or equivalent</sup></sub>",
                "University (bachelor) <sub><sup>or equivalent</sup></sub>",
                "High school",
                "Other",
            ],
            name: "education",
        },
        // {
        //     prompt: "English level",
        //     options: ["native", "fluent", "intermediate", "beginner"],
        //     name: "english",
        // },
    ],
    data: {
        screen: "demographics_1",
    },
}

var demographics_freetext = {
    type: jsPsychSurveyText,
    questions: [
        {
            prompt: "Please enter your age (in years)",
            placeholder: "e.g., '31'",
            name: "age",
        },
        {
            prompt: "Please enter your ethnicity",
            placeholder: "e.g., Caucasian",
            name: "ethnicity",
        },
    ],
    data: {
        screen: "demographics_2",
    },
}

var demographics_info = {
    timeline: [demographics_multichoice, demographics_freetext],
}

// Psychopathology ========================================================================
var demographics_disorders = {
    type: jsPsychSurveyMultiSelect,
    preamble:
        "As this study contains questions about your feelings and mood, it is important for us understand relevant medical antecedents.<br>If nothing applies to you, do not tick anything and click on 'Continue'.",
    questions: [
        {
            prompt: "<b>Are you <i>currently</i> living with one of the following medically diagnosed with any of the following?</b>",
            options: [
                "Major Depressive Disorder (MDD)",
                "Bipolar Disorder (Type I and II)",
                "Borderline Personality Disorder (BPD)",
                "Dysthymia (Persistent Depressive Disorder)",
                "Seasonal Affective Disorder (SAD)",
                "Premenstrual Dysphoric Disorder (PMDD)",
                // "Substance/Medication-Induced Mood Disorder",
                // "Mood Disorder Due to a General Medical Condition",
                // "Disruptive Mood Dysregulation Disorder",
                // "Adjustment Disorder with Depressed Mood",
                "Generalized Anxiety Disorder (GAD)",
                "Panic Disorder",
                "Social Anxiety Disorder (Social Phobia)",
                "Phobias",
                // "Agoraphobia",
                // "Separation Anxiety Disorder",
                // "Selective Mutism",
                "Obsessive-Compulsive Disorder (OCD)",
                "Post-Traumatic Stress Disorder (PTSD)",
                "Acute Stress Disorder",
            ],
            name: "disorder_diagnostic",
        },
        {
            prompt: "<b>Have you ever <i>previously</i> been diagnosed with any of the preceding?</b>",
            options: ["Yes", "No"],
            name: "disorder_history",
        },
        {
            prompt: "<b>Are you <i>currently</i> undergoing any following treatment:</b>",
            options: [
                "Antidepressant Medication <sup><sub>(e.g., PROZAC, ZOLOFT, EFFEXOR...)</sub></sup>",
                "Anxiolytic Medication <sup><sub>(e.g., XANAX, VALIUM, ...)</sub></sup>",
                "Psychotherapy/Counseling  <sup><sub>(e.g., CBT, ACT, ...)</sub></sup>",
                "Mood Stabilizers <sup><sub>(e.g., LITHIUM, LAMICTAL, ...)</sub></sup>",
                "Antipsychotic Medication <sup><sub>(e.g., RISPERDAL, SEROQUEL, ...)</sub></sup>",
                // "Cognitive Behavioral Therapy (CBT)",
                // "Electroconvulsive Therapy (ECT)",
                // "Transcranial Magnetic Stimulation (TMS)",
                "Lifestyle Changes <sup><sub>(e.g., diet, exercise, ...)</sub></sup>",
                "Mindfulness and Stress Management Techniques",
                "Alternative Therapies <sup><sub>(e.g., acupuncture, herbal remedies, ...)</sub></sup>",
                "Other",
            ],
            name: "disorder_treatment",
        },
    ],
    data: {
        screen: "demographics_disorders",
    },
}
