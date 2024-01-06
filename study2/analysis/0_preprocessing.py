import json

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

for i, file in enumerate(files):
    print(f"File N°{i+1}/{len(files)}")

    data = pd.read_csv(file["file"]._get(file["url"], stream=True).raw)

    # Participant ========================================================
    # data["screen"].unique()

    # Browser info -------------------------------------------------------
    brower = data[data["screen"] == "browser_info"].iloc[0]

    df = pd.DataFrame(
        {
            "Participant": file["name"],
            "Experimenter": brower["experimenter"],
            "Experiment_Duration": data["time_elapsed"].max() / 1000 / 60,
            "Date": brower["date"],
            "Time": brower["time"],
            "Browser": brower["browser"],
            "Mobile": brower["mobile"],
            "Platform": brower["os"],
            "Screen_Width": brower["screen_width"],
            "Screen_Height": brower["screen_height"],
        },
        index=[0],
    )

    # Demographics -------------------------------------------------------
    demo1 = data[data["screen"] == "demographics_1"].iloc[0]
    demo1 = json.loads(demo1["response"])

    df["Gender"] = demo1["gender"]

    demo2 = data[data["screen"] == "demographics_2"].iloc[0]
    demo2 = json.loads(demo2["response"])

    df["Age"] = demo2["age"]

    # Education
    edu = demo1["education"]
    edu = "Bachelor" if "bachelor" in edu else edu
    edu = "Master" if "master" in edu else edu
    edu = "Doctorate" if "doctorate" in edu else edu
    df["Education"] = edu

    # Ethnicity
    race = demo2["ethnicity"].title().rstrip()
    race = "Caucasian" if race in ["White", "White British"] else race
    race = "South Asian" if race in ["Pakistani"] else race
    race = "Arab" if race in ["Middle Eastern"] else race
    race = (
        "Arab" if race in ["Muslim"] else race
    )  # Experimenter1: Likelihood given recruitment date
    race = "Other" if race in ["Bahraini", "Manama"] else race
    df["Ethnicity"] = race

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

    # Save data ----------------------------------------------------------
    alldata = pd.concat([alldata, df], axis=0, ignore_index=True)

# Save data ==============================================================
# Inspect
alldata["Ethnicity"].unique()

# Remove columns
alldata = alldata.drop(
    columns=[
        "Time",
        "Browser",
        "Platform",
        "Screen_Width",
        "Screen_Height",
    ]
)
# Reanonimize
alldata = alldata.sort_values(by=["Date"]).reset_index(drop=True)
alldata["Participant"] = [f"S{i+1:03}" for i in alldata.index]
# Save data
alldata.to_csv("../data/data_raw.csv", index=False)
print("Done!")
