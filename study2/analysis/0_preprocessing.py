import json
import os
import numpy as np
import pandas as pd


# List files ============================================================
path = "C:/Users/domma/Box/Data/PHQ4R/"
files = os.listdir(path)


# Loop through files ======================================================
alldata = pd.DataFrame()  # Initialize empty dataframe
prolific_ids = {}

for i, file in enumerate(files):
    print(f"File N°{i+1}/{len(files)}")

    if (
        "Participant" in alldata.columns
        and file.replace(".csv", "") in alldata["Participant"].values
    ):
        continue

    data = pd.read_csv(path + file)

    # Participant ========================================================
    # data["screen"].unique()

    # Browser info -------------------------------------------------------
    browser = data[data["screen"] == "browser_info"].iloc[0]

    # Experimenter
    if "experimenter" in browser.index:
        experimenter = browser["experimenter"]
    else:
        experimenter = browser["researcher"]
    if "prolific_id" in browser.index:
        if isinstance(browser["prolific_id"], str):
            experimenter = "Prolific"
    if isinstance(experimenter, float):
        if np.isnan(experimenter):
            experimenter = "Unknown"
        else:
            experimenter = "Experimenter" + str(int(experimenter))

    df = pd.DataFrame(
        {
            "Participant": file.replace(".csv", ""),
            "Experimenter": experimenter,
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date": browser["date"],
            "Time": browser["time"],
            "Browser": browser["browser"],
            "Mobile": browser["mobile"],
            "Platform": browser["os"],
            "Screen_Width": browser["screen_width"],
            "Screen_Height": browser["screen_height"],
        },
        index=[0],
    )

    # Prolific
    if experimenter == "Prolific":
        id = browser["prolific_id"]
        if id not in []:
            prolific_ids[file.replace(".csv", "")] = id

    df["SONA_ID"] = np.nan
    if "sona_id" in browser.index:
        if np.isnan(browser["sona_id"]) == False:
            id = int(browser["sona_id"])
            df["SONA_ID"] = id

    # Filter duplicates
    if df["SONA_ID"].values[0] == 30609 and df["Experiment_Duration"].values[0] < 6:
        continue
    if df["SONA_ID"].values[0] == 30679 and df["Date"].values[0] != "22/03/2024":
        continue
    if df["SONA_ID"].values[0] == 30688 and df["Time"].values[0] != "13:02:42":
        continue
    if df["SONA_ID"].values[0] == 30746 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 30746 and df["Date"].values[0] != "19/04/2024":
        continue
    if df["SONA_ID"].values[0] == 30759 and df["Experiment_Duration"].values[0] > 10:
        continue
    if df["SONA_ID"].values[0] == 31787 and df["Experiment_Duration"].values[0] < 8:
        continue
    if df["SONA_ID"].values[0] == 30796 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 30796 and df["Experiment_Duration"].values[0] > 20:
        continue
    if df["SONA_ID"].values[0] == 30836 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 30878 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 30884 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 30913 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 30939:
        continue
    if df["SONA_ID"].values[0] == 30979 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31030 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31687 and df["Date"].values[0] != "30/04/2024":
        continue
    if df["SONA_ID"].values[0] == 31727 and df["Date"].values[0] != "26/04/2024":
        continue
    if df["SONA_ID"].values[0] == 31769 and df["Experiment_Duration"].values[0] > 15:
        continue
    if df["SONA_ID"].values[0] == 31787 and df["Experiment_Duration"].values[0] < 7:
        continue
    if df["SONA_ID"].values[0] == 31800 and df["Experiment_Duration"].values[0] < 6:
        continue
    if df["SONA_ID"].values[0] == 31811 and df["Experiment_Duration"].values[0] < 15:
        continue
    if df["SONA_ID"].values[0] == 31849 and df["Experiment_Duration"].values[0] < 10.5:
        continue
    if df["SONA_ID"].values[0] == 31886 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31888 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 30733 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31943 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31873 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31885 and (
        df["Experiment_Duration"].values[0] < 8 or df["Date"].values[0] != "27/03/2024"
    ):
        continue
    if df["SONA_ID"].values[0] == 31843 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31744 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31943 and df["Experiment_Duration"].values[0] < 12:
        continue
    if df["SONA_ID"].values[0] == 31968 and df["Experiment_Duration"].values[0] < 12:
        continue
    if df["SONA_ID"].values[0] == 31757 and df["Experiment_Duration"].values[0] < 4:
        continue
    if df["SONA_ID"].values[0] == 32176 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 32186 and df["Experiment_Duration"].values[0] < 6:
        continue
    if df["SONA_ID"].values[0] == 32004 and df["Experiment_Duration"].values[0] > 10:
        continue
    if df["SONA_ID"].values[0] == 32084 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 32030 and df["Experiment_Duration"].values[0] < 15:
        continue
    if df["SONA_ID"].values[0] == 32387 and (
        df["Date"].values[0] != "26/09/2024" or df["Experiment_Duration"].values[0] < 10
    ):
        continue
    if df["SONA_ID"].values[0] == 32428 and df["Mobile"].values[0] == False:
        continue  # Mobile was the first
    if df["SONA_ID"].values[0] == 32453 and df["Experiment_Duration"].values[0] > 10:
        continue
    if df["SONA_ID"].values[0] == 32505 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 32716 and df["Experiment_Duration"].values[0] < 8:
        continue
    if df["SONA_ID"].values[0] == 32747 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31010 and df["Experiment_Duration"].values[0] < 5:
        continue
    if df["SONA_ID"].values[0] == 31855 and df["Date"].values[0] != "27/03/2024":
        continue
    if df["SONA_ID"].values[0] == 31868 and (
        df["Experiment_Duration"].values[0] < 10 or df["Date"].values[0] != "15/03/2024"
    ):
        continue
    if df["SONA_ID"].values[0] == 32314 and df["Date"].values[0] != "07/10/2024":
        continue
    if df["SONA_ID"].values[0] == 31891 and df["Date"].values[0] != "30/09/2024":
        continue
    if df["SONA_ID"].values[0] == 32046 and df["Date"].values[0] != "10/10/2024":
        continue
    if df["SONA_ID"].values[0] == 32130 and df["Date"].values[0] != "14/10/2024":
        continue
    if df["SONA_ID"].values[0] == 32344 and df["Date"].values[0] != "17/10/2024":
        continue
    if df["SONA_ID"].values[0] == 32700 and df["Date"].values[0] != "15/10/2024":
        continue
    if df["SONA_ID"].values[0] == 32744 and df["Date"].values[0] != "19/10/2024":
        continue
    if df["SONA_ID"].values[0] == 32119 and df["Date"].values[0] != "05/03/2024":
        continue
    if df["SONA_ID"].values[0] == 32378 and df["Date"].values[0] != "27/10/2024":
        continue
    if df["SONA_ID"].values[0] == 32379 and df["Date"].values[0] != "01/11/2024":
        continue
    if df["SONA_ID"].values[0] == 32620 and df["Experiment_Duration"].values[0] > 15:
        continue
    if df["SONA_ID"].values[0] == 32769 and df["Experiment_Duration"].values[0] < 8.80:
        continue
    if df["SONA_ID"].values[0] == 32798 and df["Date"].values[0] != "30/10/2024":
        continue
    if df["SONA_ID"].values[0] == 31977 and df["Date"].values[0] != "15/03/2024":
        continue
    if df["SONA_ID"].values[0] == 32062 and df["Date"].values[0] != "28/03/2024":
        continue
    if df["SONA_ID"].values[0] == 32090 and df["Date"].values[0] != "01/05/2024":
        continue
    if df["SONA_ID"].values[0] == 32398 and df["Date"].values[0] != "09/11/2024":
        continue
    if df["SONA_ID"].values[0] == 32424 and df["Date"].values[0] != "07/11/2024":
        continue
    if df["SONA_ID"].values[0] == 32495 and df["Experiment_Duration"].values[0] < 7:
        continue
    if df["SONA_ID"].values[0] == 32524 and df["Experiment_Duration"].values[0] < 9:
        continue
    if df["SONA_ID"].values[0] == 32529 and df["Date"].values[0] != "04/11/2024":
        continue
    if df["SONA_ID"].values[0] == 32625 and df["Experiment_Duration"].values[0] < 5:
        continue
    if df["SONA_ID"].values[0] == 32629 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 32632 and df["Date"].values[0] != "04/11/2024":
        continue
    if df["SONA_ID"].values[0] == 31749 and df["Date"].values[0] != "20/11/2024":
        continue
    if df["SONA_ID"].values[0] == 31918 and df["Date"].values[0] != "02/05/2024":
        continue
    if df["SONA_ID"].values[0] == 32071 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 32121 and df["Date"].values[0] != "01/05/2024":
        continue
    if df["SONA_ID"].values[0] == 32699 and df["Date"].values[0] != "06/11/2024":
        continue
    if df["SONA_ID"].values[0] == 32769 and df["Date"].values[0] != "31/10/2024":
        continue
    if df["SONA_ID"].values[0] == 31771 and df["Experiment_Duration"].values[0] < 6:
        continue
    if df["SONA_ID"].values[0] == 31861 and df["Date"].values[0] != "30/11/2024":
        continue
    if df["SONA_ID"].values[0] == 31873 and df["Date"].values[0] != "18/03/2024":
        continue
    if df["SONA_ID"].values[0] == 31875 and df["Experiment_Duration"].values[0] < 3:
        continue
    if df["SONA_ID"].values[0] == 32340 and df["Experiment_Duration"].values[0] < 3:
        continue
    if df["SONA_ID"].values[0] == 32742 and df["Date"].values[0] != "03/12/2024":
        continue

    # Demographics -------------------------------------------------------
    demo1 = data[data["screen"] == "demographics_1"].iloc[0]
    demo1 = json.loads(demo1["response"])

    sex = demo1["gender"]
    df["Gender"] = np.nan if sex == "" else sex

    demo2 = data[data["screen"] == "demographics_2"].iloc[0]
    demo2 = json.loads(demo2["response"])

    age = demo2["age"]
    age = 63 if age == "Sixty three" else age
    age = 28 if age == "É8" else age
    age = 19 if age == "'19'" else age
    age = np.nan if age == 12 else age  # Sona participant (> 18)
    df["Age"] = np.nan if age == "" else float(age)

    # Education
    edu = demo1["education"]
    edu = "High School" if "High school" in edu else edu
    edu = "Bachelor" if "bachelor" in edu else edu
    edu = "Master" if "master" in edu else edu
    edu = "Doctorate" if "doctorate" in edu else edu
    edu = np.nan if edu == "" in edu else edu
    df["Education"] = edu

    # Ethnicity
    race = demo2["ethnicity"].lower().rstrip().lstrip()
    race = (
        "White"
        if race
        in [
            "white",
            "white british",
            "white english",
            "white brit",
            "british",
            "british white",
            "white caucasian",
            "caucasian/white european",
            "caucasian (white british)",
            "caucasion",
            "causasian",
            "caucasian",
            "white european",
            "romanian",
            "causican",
            "white (british)",
            "spicy white",
            "white, british",
            "white - british",
            "white - english",
            "white welsh",
            "british - white",
            "white- other",
            "italian",
            "caucaian",
            "serbian",
            "causcasian",
            "white other",
            "european",
            "english",
            "ukrainian",
            "native american and armenian",
            "white - other",
            "white- german and british",
            "polish",
            "white - scottish",
            "bulgarian",
            "uk",
            "slavic",
            "british, white",
            "caucaisan",
            "cuacasian",
            "portuguese",
            "white-british",
        ]
        else race
    )
    race = (
        "South Asian"
        if race
        in [
            "pakistani",
            "indian",
            "asian indian",
            "srilankan",
            "nepalese",
            "british pakistani",
            "south asian",
            "sri lankan",
            "indian-asian",
        ]
        else race
    )
    race = (
        "Asian"
        if race
        in [
            "chinese",
            "asian",
            "chinese asian",
            "east asian",
            "chineese",
            "chinese, asian",
            "british-asian",
            "southeast asian",
            "other asian background",
            "british chinese",
            "asian british",
            "british asian",
            "white - irish",
        ]
        else race
    )
    race = "Hispanic" if race in ["hispanic", "latina"] else race
    race = (
        "Middle Eastern"
        if race
        in [
            "middle eastern",
            "turkish",
            "north african",
            "bangladeshi",
            "lebanese",
            "afghan",
            "arab",
            "persian",
            "arabic",
        ]
        else race
    )
    race = (
        "Middle Eastern" if race in ["muslim"] else race
    )  # Experimenter1: Likelihood given recruitment date and country of dissemination
    race = (
        "Black"
        if race
        in [
            "black",
            "african",
            "sudanese",
            "black british",
            "black african caribbean",
            "black british/african",
            "black/african/caribbean/black british",
            "black african",
            "black caribbean",
            "black/british other",
            "black british caribbean",
        ]
        else race
    )
    race = (
        "Other"
        if race
        in [
            "cypriot",
            "bahraini",
            "manama",
            "filipino",
            "white filipino",
            "tatar",
            "mediterranean",
            "barabdos",
        ]
        else race
    )
    race = "Mixed" if "mixed" in race else race
    race = (
        "Mixed"
        if race
        in [
            "white/asian",
            "white and black caribbean",
            "white and black carribean",
            "white and latino",
            "white and asian",
            "white & asian",
            "white and black african",
            "caucasian, asian white",
            "asian, caucasian",
        ]
        else race
    )
    race = np.nan if race in ["", "po]]", "wasian", "not sure"] else race
    df["Ethnicity"] = race

    # Mood disorders
    demo3 = data[data["screen"] == "demographics_disorders"].iloc[0]
    demo3 = json.loads(demo3["response"])
    df["Disorder_MDD"] = (
        1 if "Major Depressive Disorder (MDD)" in demo3["disorder_diagnostic"] else 0
    )
    df["Disorder_Bipolar"] = (
        1 if "Bipolar Disorder (Type I and II)" in demo3["disorder_diagnostic"] else 0
    )
    df["Disorder_BPD"] = (
        1
        if "Borderline Personality Disorder (BPD)" in demo3["disorder_diagnostic"]
        else 0
    )
    df["Disorder_Dysthymia"] = (
        1
        if "Dysthymia (Persistent Depressive Disorder)" in demo3["disorder_diagnostic"]
        else 0
    )
    df["Disorder_SAD"] = (
        1 if "Seasonal Affective Disorder (SAD)" in demo3["disorder_diagnostic"] else 0
    )
    df["Disorder_PMDD"] = (
        1
        if "Premenstrual Dysphoric Disorder (PMDD)" in demo3["disorder_diagnostic"]
        else 0
    )
    df["Disorder_GAD"] = (
        1 if "Generalized Anxiety Disorder (GAD)" in demo3["disorder_diagnostic"] else 0
    )
    df["Disorder_Panic"] = 1 if "Panic Disorder" in demo3["disorder_diagnostic"] else 0
    df["Disorder_SocialPhobia"] = (
        1
        if "Social Anxiety Disorder (Social Phobia)" in demo3["disorder_diagnostic"]
        else 0
    )
    df["Disorder_Phobia"] = 1 if "Phobias" in demo3["disorder_diagnostic"] else 0
    df["Disorder_OCD"] = (
        1
        if "Obsessive-Compulsive Disorder (OCD)" in demo3["disorder_diagnostic"]
        else 0
    )
    df["Disorder_PTSD"] = (
        1
        if "Post-Traumatic Stress Disorder (PTSD)" in demo3["disorder_diagnostic"]
        else 0
    )
    df["Disorder_Stress"] = (
        1 if "Acute Stress Disorder" in demo3["disorder_diagnostic"] else 0
    )

    df["DisorderHistory"] = (
        demo3["disorder_history"][0] if len(demo3["disorder_history"]) > 0 else np.nan
    )

    df["DisorderTreatment_Antidepressant"] = (
        1 if any(["Antidepressant" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Anxiolytic"] = (
        1 if any(["Anxiolytic" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Therapy"] = (
        1 if any(["Psychotherapy" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_MoodStabilizer"] = (
        1 if any(["Mood Stabilizer" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Antipsychotic"] = (
        1 if any(["Antipsychotic" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Lifestyle"] = (
        1 if any(["Lifestyle" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Mindfulness"] = (
        1 if any(["Mindfulness" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Alternative"] = (
        1 if any(["Alternative" in i for i in demo3["disorder_treatment"]]) else 0
    )
    df["DisorderTreatment_Other"] = (
        1 if any(["Other" in i for i in demo3["disorder_treatment"]]) else 0
    )

    # Questionnaires =====================================================

    # Questionnaire Order ------------------------------------------------
    # Select all screens start _with 'questionnaire'
    order = list(data[data["screen"].str.startswith("questionnaire")]["screen"])

    # PHQ4 ---------------------------------------------------------------
    phq4 = data[data["screen"] == "questionnaire_phq4"].iloc[0]

    df["PHQ4_Condition"] = (
        "PHQ4 - Revised" if phq4["condition"] == "PHQ4R" else "PHQ4 - Original"
    )

    df["PHQ4_Duration"] = phq4["rt"] / 1000 / 60
    df["PHQ4_Order"] = order.index("questionnaire_phq4") + 1

    phq4 = json.loads(phq4["response"])
    for item in phq4:
        df[item] = phq4[item]

    # STAI ---------------------------------------------------------------
    stai = data[data["screen"] == "questionnaire_stai5"].iloc[0]

    df["STAI5_Duration"] = stai["rt"] / 1000 / 60
    df["STAI5_Order"] = order.index("questionnaire_stai5") + 1

    stai = json.loads(stai["response"])
    for item in stai:
        df[item] = stai[item]

    # BDI-2 --------------------------------------------------------------
    bdi2 = data[data["screen"] == "questionnaire_bdi2"].iloc[0]

    df["BDI2_Duration"] = bdi2["rt"] / 1000 / 60
    df["BDI2_Order"] = order.index("questionnaire_bdi2") + 1

    bdi2 = json.loads(bdi2["response"])
    for item in bdi2:
        resp = bdi2[item][0:3]
        # Keep only number in string
        df[item] = int(resp.join([i for i in resp if i.isdigit()]))

    # IAS ----------------------------------------------------------------
    ias = data[data["screen"] == "questionnaire_ias"].iloc[0]

    df["IAS_Duration"] = ias["rt"] / 1000 / 60
    df["IAS_Order"] = order.index("questionnaire_ias") + 1

    ias = json.loads(ias["response"])
    for item in ias:
        df[item] = ias[item]

    # Defragment DF
    df = df.copy()

    # MAIA ----------------------------------------------------------------
    if "questionnaire_maia" in order:
        maia = data[data["screen"] == "questionnaire_maia"].iloc[0]
        df["MAIA_Duration"] = maia["rt"] / 1000 / 60
        df["MAIA_Order"] = order.index("questionnaire_maia") + 1

        maia = json.loads(maia["response"])
        for item in maia:
            df[item] = maia[item]

    # Save data ----------------------------------------------------------
    alldata = pd.concat([alldata, df], axis=0, ignore_index=True, join="outer")

# Save data ==============================================================


# Remove columns
alldata = alldata.drop(
    columns=[
        "Browser",
        "Platform",
        "Screen_Width",
        "Screen_Height",
    ]
)

# Reanonimize ============================================================
alldata["d"] = pd.to_datetime(
    alldata["Date"] + " " + alldata["Time"], format="%d/%m/%Y %H:%M:%S"
)
alldata = alldata.sort_values(by=["d"]).reset_index(drop=True)
correspondance = {j: f"S{i+1:03}" for i, j in enumerate(alldata["Participant"])}
alldata["Participant"] = [correspondance[i] for i in alldata["Participant"]]
alldata = alldata.drop(columns=["d"])  # Drop OSf column


# Prolific ============================================================
prolific_ids = {correspondance[k]: v for k, v in prolific_ids.items()}
# prolific_ids
# "59dcaf7124d7bf00012f09c4" in [prolific_ids[i] for i in prolific_ids.keys()]

# SONA check ================================================================
sona_credited = [
    29640,
    29636,
    29659,
    29761,
    29829,  # Check 3 Failed
    29903,
    29913,
    30018,
    30609,
    30610,  # Not in the list
    30611,
    30615,
    30616,
    30617,  # Check 2 failed
    30624,
    30626,
    30627,
    30631,
    30636,
    30652,
    30656,
    30665,
    30682,
    30690,
    30697,
    30712,  # Not in list
    30733,  # Not in list Check 3 failed
    30742,
    30743,
    30744,
    30745,
    30746,
    30747,  # Not in list
    30748,
    30758,
    30759,  # Not in list
    30761,
    30765,
    30770,
    30783,  # Check 3 Failed
    30796,  # Check 3 Failed
    30798,
    30799,
    30834,
    30838,
    30846,  # Check 3 failed (awarded because email)
    30863,  # Not in list
    30867,
    30873,
    30878,  # Not in list - Check 3 failed
    30835,
    30909,
    30913,  # Failed checks
    30926,
    30930,  # Check 3 failed
    30939,  # Check fails
    30942,
    30957,  # Check 3 failed
    30970,
    30974,  # Not in list
    30979,
    30981,  # Not in list
    30986,
    31005,  # Check 3 Failed
    31008,
    31009,
    31010,  # Not in list
    31013,
    31017,
    31030,
    31038,
    31043,
    31048,
    31075,
    31082,
    31108,
    31673,
    31687,
    31726,  # failed checks
    31727,
    31732,
    31736,  # check 3 failed
    31742,
    31753,
    31758,
    31761,
    31762,
    31764,  # check 2 failed
    31767,
    31768,
    31769,
    31770,
    31772,
    31779,
    31783,
    31788,  # check 2 failed
    31793,
    31799,
    31800,
    31801,  # Check 3 Failed
    31803,
    31804,
    31807,
    31809,
    31811,
    31812,
    31817,
    31821,
    31826,
    31829,  # Not in list
    31831,
    31833,
    31839,
    31840,
    31845,  # Check 3 failed
    31849,
    31850,
    31851,
    31853,  # Failed check 3
    31854,
    31855,  # Not in list
    31856,
    31857,
    31859,
    31862,
    31864,
    31868,
    31872,
    31873,  # Not in list - Check 3 Failed
    31880,
    31885,  # Not in list - Check 3 Failed
    31888,
    31893,
    31899,
    31902,
    31903,  # Checks failed
    31905,
    31909,  # Check 3 failed
    31911,
    31918,  # Check 2 failed
    31923,
    31925,
    31930,
    31932,
    31934,  # Check 3 failed
    31937,
    31955,
    31960,  # Check 3 failed
    # 31961,  Not in list?
    31963,
    31972,
    31976,
    31978,
    31984,  # Check 3 Failed
    # 31989, # Not in list
    32001,
    32007,
    32009,  # check 3 failed
    32014,
    32023,
    32025,
    32031,
    32034,
    32037,
    # 32038, # Not in list
    32042,
    32045,
    32052,
    32054,
    32058,
    32066,
    32069,
    32082,
    32090,
    32093,
    32094,  # Check 3 failed
    32096,
    32107,  # Check 3 Failed
    32109,
    32121,
    32130,
    32133,  # Check 3 failed
    32143,
    32146,  # Check 3 failed
    32148,  # Check 3 failed
    32154,  # check 3 failed
    32160,
    32161,
    32162,
    32165,  # Check 3 failed
    32175,
    32176,  # Check 3 failed
    32179,
    32180,
    32187,
    32188,  # Check 3 failed
    32286,  # Check 3 failed
    32287,
    32293,
    32301,
    32306,  # Check 3 failed
    32312,
    32313,
    32321,  # Check 3 failed
    32337,
    32341,
    32344,
    32345,
    32348,
    32358,  # Check 3 failed
    32362,  # Check 3 failed
    32365,
    32367,  # Check 3 failed
    32376,
    32380,
    32382,
    32385,
    32387,
    32396,
    32399,
    32401,
    32408,
    32416,
    32418,
    32417,  # Check 3 failed
    32423,
    32428,
    32429,
    32433,
    32441,
    32442,  # Check 3 failed
    32444,
    32448,  # Check 3 failed
    32449,
    32451,
    32452,
    32453,
    32458,
    32464,
    32469,
    32470,
    32471,  # Check 3 failed
    32477,
    32488,  # Check 3 failed
    32491,
    32484,
    32497,
    32502,
    # 32505, # check failed (not in list)
    32508,
    32510,
    32522,
    32533,
    32534,  # Check 3 failed
    32541,
    32544,  # Check 3 failed
    32559,
    32569,
    32572,
    32576,
    32578,
    32591,
    32593,  # Check 3 failed
    32601,  # Check 3 failed
    32603,
    32605,
    32604,
    32608,
    # 32611, # Check 3 failed Not i n list
    # 32615, # Not in l ist
    32619,
    32634,
    32635,  # Check 1 failed
    32642,
    32643,
    32646,
    32650,
    32651,
    32652,  # Failed checks
    32658,
    32663,
    32664,
    32668,  # Check 2 failed
    32670,
    32673,
    32675,  # Check 3 failed
    32676,
    32679,
    32683,  # Check 3 failed
    32684,
    32686,
    32691,
    32693,  # Check 3 failed
    # 32700, Not in list
    32703,
    32704,  # Check 3 failed
    32705,
    32708,
    32710,
    32716,  # Check 2 failed
    32718,
    32721,
    32722,  # Check 3 failed
    32723,  # Check 3 failed
    32729,  # Checks failed
    32735,
    32740,  # Check 3 failed
    32744,
    32747,
    32753,
    32761,  # Check 3 failed
    32762,
    32770,
    32773,
    32779,
    32780,
    32784,
    30738,
    30786,
    30724,
    30736,
    30782,
    32783,
    32796,
    30813,
    30884,
    31886,
    31011,
    31019,
    31034,
    31060,
    31086,  # Check 3 failed
    31110,
    31723,
    31744,
    31745,
    31752,
    31759,
    31774,
    31777,
    31782,
    31787,
    31796,
    31805,
    31816,
    31820,
    31824,
    31827,
    31835,
    31838,
    31852,  # Check 2 failed
    31865,
    31869,
    31871,  # Check 3 failed
    31876,
    31883,
    31889,
    31894,
    31906,
    31915,
    31916,
    31919,
    31926,
    31929,
    31943,
    31957,
    31959,
    31968,
    31973,
    31975,
    31977,  # Not in the list
    31981,
    31991,
    32003,  # Not in list
    32004,  # Not in list
    32015,
    32019,
    32022,
    32039,
    32041,
    32047,
    32051,
    32055,
    32057,
    32059,
    32062,  # Not in the list
    32067,
    32077,  # Check 3 failed
    32080,
    32083,
    32088,
    32091,
    32098,
    32105,
    32106,
    32113,
    32114,
    32119,
    32120,
    32152,  # Not in the list
    32168,
    32173,
    32181,
    32183,
    32244,
    32132,
    30615,
    30687,
    32173,
    32178,
    32189,  # Check 2 failed
    32247,
    30708,
    # 30712, # Not in the list
    30751,
    30819,
    30840,
    30892,
    30904,
    30978,
    30985,
    31011,
    # 31019, # Not in the list
    31047,
    31066,
    31115,
    31776,
    # 31796, # Not in the list
    # 31838, # Not in the list
    31844,
    31867,
    31878,
    31935,
    31948,
    31956,
    31957,
    # 31959, # Not in the list
    31965,
    # 31977, # Not in the list
    32002,
    32016,
    32026,
    32051,
    # 32055, # Not in the list
    32072,  # Failed check 3
    # 32083, # Not in the list
    # 32091, # not in the list
    # 32113, # not in the list
    32115,
    # 32119, # not in the list
    30640,
    30898,
    30794,
    31064,
    31098,
    31729,
    31781,  # failed Check 3
    31874,
    31941,
    31947,
    31977,
    32011,
    32013,
    32030,  # failed check 3
    32064,
    32108,
    32142,
    31757,  # failed check 3
    30679,
    32084,
    32186,
    # ana gave credits from this number on the 7/05
    29661,
    30624,
    30626,
    30631,
    30652,
    30669,
    32182,
    32185,
    32187,
    # 32189. attention 2 check = 0 ,
    # 32191, not on the list
    # 32176, did more than once, failed check 3 on one occasion
    30688,
    30719,
    30720,
    # 30733, did study twice failed attention check 3 once
    32151,
    31901,
    31016,
    32155,
    31892,
    # 31751 failed check 2?
    31884,
    30870,  # failed check 3
    30880,
    32123,
    #  31958 failed check 2?
    31966,  # failed check 3
    30940,
    32163,
    32073,
    31737,  # failed check 3
    31946,  # failed check 3
    30947,
    # 30939 did study multiple times, failed attention checks as well
    31841,
    31050,
    31733,  # failed attention check 3
    32018,  # failed attention check 3
    31992,
    31970,
    31879,
    32048,
    30895,
    31836,  # failed attention check 3
    31102,  # failed attention check 3
    32158,  # failed attention check 3
    32017,
    31842,
    31877,
    30836,  # did experiment twice but passed all checks
    32129,
    32174,
    31942,  # failed attention check 3
    30998,
    30704,  # not on the list
    30761,
    30799,
    31814,
    30835,
    30838,
    # 30846,  # was given credit but failed attention check 3?
    31863,
    30873,
    30896,
    30909,
    30926,
    31008,
    31009,
    31017,
    31038,
    31043,
    # 31075, not on the list
    # 31687, not on the list
    31726,
    31731,
    31732,
    31739,
    31746,
    31751,  # failed check 2 potentially check 3
    # 31761, # was given credit but failed attention check 3?
    31775,
    31816,
    31817,
    31784,  # failed attention check 3
    31785,
    31808,
    31826,
    31830,
    31834,
    31843,
    31859,
    # 31891, # Not in list
    31893,
    31899,
    31905,
    31920,  # failed attention check 3
    31923,
    31928,
    31930,
    31944,
    31950,
    31958,  # failed attention check 2
    31961,
    31967,
    31974,
    # 31984, it was given credit ut failed check 3?
    32007,
    32024,
    32025,
    32029,
    32034,
    32042,
    32046,
    32050,
    32054,
    32056,
    32065,
    32074,
    32076,
    32078,
    32085,
    32097,
    32099,
    32116,
    32122,
    32154,
    32162,
    32184,
    32191,
    32260,  # failed attention check 3
    32294,  # failed attention check 3
    32305,
    32314,
    32322,
    32330,
    32331,
    32351,
    32368,
    32374,  # failed attention check 3
    32377,
    32378,
    32379,
    32386,
    32403,
    32406,
    32410,  # failed attention check 3
    32426,
    32456,
    32457,
    32462,
    32468,
    32476,  # failed attention check 2
    32485,
    32486,
    32494,  # failed attention check 3
    32498,
    32500,
    32511,  # failed attention check 2
    32516,
    32547,  # failed attention check 3
    32556,
    32561,
    32567,
    32568,  # failed attention check 3
    32570,  # failed attention check 3
    32571,  # failed attention checks
    32577,  # failed attention check 3
    32579,
    32582,  # failed attention check 3
    32583,
    32612,
    32616,
    32620,
    32631,
    32638,
    32641,
    32653,
    32672,
    32680,  # failed attention check 3
    32695,  # failed attention check 3
    32698,
    32711,
    32715,  # failed attention check 3
    32724,
    32726,
    32731,
    32734,
    32743,  # failed attention check 3
    32745,
    32749,  # failed attention check 3
    32757,
    32758,
    32765,  # failed attention check 3
    32772,  # failed attention check 3
    32798,  # Failed attention check 3
    # 13/11/2024
    31763,
    31791,
    31881,
    31914,  # failed attention check 3
    31939,
    31954,  # failed attention check 3
    31985,
    31997,
    32027,  # failed attention check 1
    32111,
    32145,
    32172,
    32252,
    32289,
    32290,
    32296,  # failed attention check 3
    32307,
    32318,  # failed attention check 3
    32329,
    32352,  # failed attention check 3
    32353,
    32360,  # failed attention check 3
    32366,  # failed attention check 3
    32372,
    32383,
    32388,  # failed attention check 3
    32393,
    32394,
    32398,  # failed attention check 3
    32412,
    32424,
    32425,  # failed attention check 3
    32432,
    32446,
    32465,
    32474,
    32480,
    32481,
    32483,
    32495,
    32505,  # failed attention check 3
    32507,  # failed attention check 3
    32513,
    32517,
    32523,
    32524,
    32529,
    32536,
    32563,  # failed attention check 3
    32564,  # failed attention check 3
    32566,  # failed attention check 3
    32606,
    32622,
    32625,  # failed attention check 3
    32629,
    32632,
    32647,
    32657,
    32665,
    32713,
    32727,
    32764,
    32776,  # failed attention check 3
    31741,
    31895,
    32138,
    32291,
    32405,
    32450,
    32493,
    32737,
    # 25/11/2024
    30634,
    31015,
    31738,
    31749,
    31778,
    31846,  # failed attention check 3
    31994,
    32036,
    32125,
    32303,
    32381,  # failed attention check 3
    32389,
    32411,  # failed attention checks
    32413,
    32419,  # failed attention check 3
    32422,  # failed attention check 3
    32436,
    32437,  # failed attention check 3
    32443,  # failed attention check 3
    32447,  # failed attention checks
    32475,
    32478,
    32504,
    32519,
    32525,
    32586,
    32589,
    32602,  # failed attention checks
    32618,
    32648,
    32667,  # failed attention check 1
    32687,
    32690,
    32733,
    32738,
    32759,  # failed attention checks
    32760,  # failed attention check 3
    32777,
    32781,
    # 03/12/2024
    30672,
    31861,
    31900,
    31969,  # failed attention check 3
    32012,  # failed attention check 3
    32071,  # failed attention checks
    32232,
    32309,
    32317,  # failed attention check 3
    32319,
    32339,
    32343,
    32392,  # failed attention check 3
    32467,  # failed attention check 3
    32472,
    32490,
    32550,  # failed attention check 3
    32554,
    32555,
    32609,
    32610,  # failed attention check 3
    32627,
    32630,
    32633,  # failed attention check 3
    32678,  # failed attention check 3
    32697,
    32717,
    32748,
    32763,  # failed attention check 3
    32814,  # failed attention check 2
    # 06/12/2024
    31743,
    31875,
    31983,
    32028,
    32053,
    32087,
    32134,
    32346,
    32361,
    32420,
    32509,
    32573,  # failed attention check 3
    32587,
    32656,  # failed attention check 3
    32742,  # failed attention check 3
    # NOT IN LIST ----------
    # 32118,
    31918,
    32038,
    32068,
    32090,
    31771,
    31989,
    31891,
    32118,
    32121,
    32349,
    32375,
    32397,
    32585,
    32611,  # failed attention check 3
    32615,
    32699,  # failed attention check 3
    32700,
    32769,
]


# Inspection ============================================================
pd.set_option("display.max_rows", None)

sona = (
    alldata[~np.isnan(alldata["SONA_ID"])]
    .sort_values("SONA_ID")
    .set_index("SONA_ID", drop=False)
)

ids = list(np.sort(sona["SONA_ID"].astype(int).values))
sona.loc[
    [id for id in ids if id not in sona_credited],
    [
        "AttentionCheck_2",
        "AttentionCheck_3",
        "Date",
        "Time",
        "Experiment_Duration",
        "Mobile",
    ],
]
# Inspect specific ppt
sona.loc[sona["SONA_ID"] == 32377,]


# Find duplicates
duplicates = (
    alldata["SONA_ID"].value_counts()[alldata["SONA_ID"].value_counts() > 1].index
)
alldata.loc[
    [True if id in duplicates.tolist() else False for id in alldata["SONA_ID"].values],
    [
        "SONA_ID",
        "AttentionCheck_2",
        "AttentionCheck_3",
        "Date",
        "Time",
        "Experiment_Duration",
        "Mobile",
    ],
].sort_values(["SONA_ID", "Date", "Time"])


# Inspect
alldata["Ethnicity"].unique()


# Save data ==============================================================
alldata.to_csv("../data/data_raw.csv", index=False)
print("Done!")
