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


token = "zYboMoukFI8HKabenQ35DH6tESHJo6oZll5BvOPma6Dppjqc2jnIB6sPCERCuaqO0UrHAa"  # Paste OSF token here to access private repositories
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

    if (
        "Participant" in alldata.columns
        and file["name"] in alldata["Participant"].values
    ):
        continue

    download_ok = False
    while download_ok == False:
        data = pd.read_csv(file["file"]._get(file["url"], stream=True).raw)
        if len(data) > 0:
            download_ok = True

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

    # Filter duplicates
    if df["SONA_ID"].values[0] == 30609 and df["Experiment_Duration"].values[0] < 6:
        continue
    if df["SONA_ID"].values[0] == 30679 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 30746 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 30878 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 30884 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 30913 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31769 and df["Experiment_Duration"].values[0] > 15:
        continue
    if df["SONA_ID"].values[0] == 31811 and df["Experiment_Duration"].values[0] < 15:
        continue
    if df["SONA_ID"].values[0] == 31886 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 30733 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31943 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31873 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31885 and df["Experiment_Duration"].values[0] < 8:
        continue
    if df["SONA_ID"].values[0] == 31744 and df["Experiment_Duration"].values[0] < 10:
        continue
    if df["SONA_ID"].values[0] == 31943 and df["Experiment_Duration"].values[0] < 12:
        continue
    if df["SONA_ID"].values[0] == 31968 and df["Experiment_Duration"].values[0] < 12:
        continue
    if df["SONA_ID"].values[0] == 31757 and df["Experiment_Duration"].values[0] < 4:
        continue
    if df["SONA_ID"].values[0] == 32186 and df["Experiment_Duration"].values[0] < 6:
        continue
    if df["SONA_ID"].values[0] == 32004 and df["Experiment_Duration"].values[0] > 10:
        continue
    if df["SONA_ID"].values[0] == 32084 and df["Mobile"].values[0] == True:
        continue
    if df["SONA_ID"].values[0] == 32030 and df["Experiment_Duration"].values[0] < 15:
        continue
    if df["SONA_ID"].values[0] == 31010 and df["Experiment_Duration"].values[0] < 5:
        continue
    if df["SONA_ID"].values[0] == 31868 and df["Experiment_Duration"].values[0] < 10:
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
    30018,  # not in tlist
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
    # 30733,
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
    30942,
    30957,  # Check 3 failed
    30970,
    30974,  # Not in list
    30981,  # Not in list
    30986,
    31005,  # Check 3 Failed
    31008,
    31009,
    31010,  # Not in list
    31013,
    31017,
    31038,
    31043,
    31048,
    31082,
    31108,
    31673,
    31726,  # failed checks
    31727,  # not in the list
    31732,
    31736,  # check 3 failed
    31761,
    31764,  # check 2 failed
    31769,
    31770,
    31772,
    31779,
    31793,
    31799,
    31801,  # Check 3 Failed
    31804,
    31809,
    31811,
    31817,
    31821,
    31826,
    31829,  # Not in list
    31833,
    31839,
    31840,
    31855,  # Not in list
    31859,
    31862,
    31868,  # Not in list
    31872,
    31873,  # Not in list - Check 3 Failed
    31885,  # Not in list - Check 3 Failed
    31893,
    31899,
    31902,
    31905,
    31923,
    31930,
    31955,
    31976,
    31978,
    31984,  # Check 3 Failed
    32007,
    32023,
    32025,
    32034,
    32042,
    32045,
    32054,
    32107,  # Check 3 Failed
    32154,  # check 3 failed
    32162,
    32175,
    32187,
    30786,
    30724,
    30736,
    30782,
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
    32022,
    32039,
    32041,
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
    # 31977 not on the list
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
    30870, # failed check 3
    30880,
    32123, 
    #  31958 failed check 2?
    31966, # failed check 3
    30940, 
    32163, 
    32073, 
    31737, # failed check 3
    31946, # failed check 3
    30947, 
    # 30939 did study multiple times, failed attention checks as well
    31841, 
    31050,
    31733, # failed attention check 3
    32018, # failed attention check 3
    31992,
    31970,
    31879, 
    32048, 
    30895, 
    31836, # failed attention check 3
    31102, # failed attention check 3
    32158, # failed attention check 3
    32017, 
    31842,
    31877, 
    30836, # did experiment twice but passed all checks
    32129, 
    32174, 
    31942, # failed attention check 3 
    30998, 
    30761,
    30799, 
    30835,
    30838, 
    # 30846,  # was given credit but failed attention check 3?
    30873, 
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
    31732, 
    31751, # failed check 2 potentially check 3
    #31761, # was given credit but failed attention check 3?
    31816, 
    31817,
    31826, 
    31859, 
    31893, 
    31899, 
    31905, 
    # 31918, not in the list
    31920, # failed attention check 3
    31923, 
    31930, 
    31958, # failed attention check 2
    # 31984, it was given credit ut failed check 3? 
    32007, 
    32025, 
    32034, 
    32042, 
    32054, 
    # 32090, not in the list
    # 32121, not in the list
    32154, 
    32162, 
    32191, 


]
pd.set_option('display.max_rows', None) 

sona = (
    alldata[~np.isnan(alldata["SONA_ID"])]
    .sort_values("SONA_ID")
    .set_index("SONA_ID", drop=False)
)

ids = list(np.sort(sona["SONA_ID"].astype(int).values))
sona["Experiment_Duration"]
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
# Inspect ppt
sona.loc[sona["SONA_ID"] == 31943,]

# Find duplicates
alldata["SONA_ID"].value_counts()[alldata["SONA_ID"].value_counts() > 1]
# Inspect duplicates
# alldata[alldata["SONA_ID"] == 31744]


# Save data
alldata.to_csv("../data/data_raw.csv", index=False)
print("Done!")
