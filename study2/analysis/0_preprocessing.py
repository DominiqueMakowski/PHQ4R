import json

import numpy as np
import pandas as pd


# Get files from OSF ======================================================
def osf_listfiles(data_subproject="", token="", after_date=None):
    try:
        import osfclient
    except ImportError:
        raise ImportError("Please install 'osfclient' (`pip install osfclient`)")
    osf = osfclient.OSF(token=token).project(data_subproject)  # Connect to project
    storage = [s for s in osf.storages][0]  # Access storage component
    files = [
        {
            "name": file.name.replace(".csv", ""),
            "date": pd.to_datetime(file.date_created),
            "url": file._download_url,
            "size": file.size,
            "file": file,
        }
        for file in storage.files
    ]

    if after_date is not None:
        date = pd.to_datetime(after_date, format="%d/%m/%Y", utc=True)
        files = [f for f, d in zip(files, [f["date"] > date for f in files]) if d]
    return files


token = ""  # Paste OSF token here to access private repositories
files = osf_listfiles(
    token=token,
    data_subproject="au695",  # Data subproject ID
    after_date="18/12/2023",
)


# Loop through files ======================================================
alldata = pd.DataFrame()  # Initialize empty dataframe
prolific_ids = {}

for i, file in enumerate(files):
    print(f"File N°{i+1}/{len(files)}")

    data = pd.read_csv(file["file"]._get(file["url"], stream=True).raw)

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
            "Participant": file["name"],
            "Experimenter": experimenter,
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date_OSF": file["date"],
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
            prolific_ids[file["name"]] = id

    df["SONA_ID"] = np.nan
    if "sona_id" in browser.index:
        if np.isnan(browser["sona_id"]) == False:
            id = int(browser["sona_id"])
            df["SONA_ID"] = id

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
    race = demo2["ethnicity"].title().rstrip()
    race = "Caucasian" if race in ["White", "White British", "White English"] else race
    race = "South Asian" if race in ["Pakistani"] else race
    race = "Arab" if race in ["Middle Eastern"] else race
    race = (
        "Arab" if race in ["Muslim"] else race
    )  # Experimenter1: Likelihood given recruitment date
    race = "Other" if race in ["Bahraini", "Manama"] else race
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
df.filter(regex=r"Disorder_", axis=1)
# Inspect
alldata["Ethnicity"].unique()


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
alldata = alldata.drop(columns=["Date_OSF", "d"])  # Drop OSf column


# Prolific ============================================================
prolific_ids = {correspondance[k]: v for k, v in prolific_ids.items()}
# prolific_ids
# "59dcaf7124d7bf00012f09c4" in [prolific_ids[i] for i in prolific_ids.keys()]

# SONA check ================================================================
sona_credited = [
    29640,
    29659,
    29761,
    29829,  # Check 3 Failed
    29903,
    # 30610,  # Not in the list
    30636,
    30743,
    30783, # Check 3 Failed 
    30942,
    30970,
    30986,
    31005, # Check 3 Failed
    31048,
    31108,
    31770,
    31779,
    31799,
    31801, # Check 3 Failed 
    31809, 
    31821,
    31839, 
    31862,  
    31902,
    31955, 
    31976, 
    31978,
    32023, 
    32045, 
    32107, # Check 3 Failed 
    32175, 
    30786,
    30665,
    30724,
    30736,
    30782,
    30813,
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
    31820,
    31824,
    31827,
    31835,
    31852,  # Check 2 failed
    31865,
    31869,
    31871,  # Check 3 failed
    31906,
    31915,
    31975,
    32057,
    32067,
    32077,  # Check 3 failed
    32098,
    32168,
    32244,
    32132, 
    30615,
    30687,
    32173,
    32178,
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
    32072, # Failed check 3
    # 32083, # Not in the list
    # 32091, # not in the list
    # 32113, # not in the list
    32115, 
    # 32119, # not in the list

    

]
sona = (
    alldata[~np.isnan(alldata["SONA_ID"])]
    .sort_values("SONA_ID")
    .set_index("SONA_ID", drop=False)
)
ids = list(np.sort(sona["SONA_ID"].astype(int).values))
sona["Experiment_Duration"]
sona.loc[
    [id for id in ids if id not in sona_credited],
    sona.columns.str.startswith("Attention"),
]



# Save data
alldata.to_csv("../data/data_raw.csv", index=False)
print("Done!")
