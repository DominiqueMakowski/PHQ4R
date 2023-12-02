import json
import os

import osfclient
import pandas as pd

token = ""  # Paste OSF token here to access private repositories
data_subproject = "au695"  # Data subproject ID
data_all = pd.DataFrame()  # Initialize empty dataframe

osf = osfclient.OSF(token=token).project(data_subproject)  # Connect to project
storage = [s for s in osf.storages][0]  # Access storage component
n_files = sum([1 for _ in storage.files])
for i, file in enumerate(storage.files):
    print(f"File N°{i+1}/{n_files}")
    file_name = file.name.replace(".csv", "")
    response = file._get(file._download_url, stream=True)
    data = pd.read_csv(response.raw)

    # Collection date
    if data["date"][0] < "17/11/2023":
        continue

    # Participant ========================================================
    # data["screen"].unique()

    # Browser info -------------------------------------------------------
    brower = data[data["screen"] == "browser_info"].iloc[0]

    df = pd.DataFrame(
        {
            "Participant": file_name,
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
    df["Education"] = demo1["education"]

    demo2 = data[data["screen"] == "demographics_2"].iloc[0]
    demo2 = json.loads(demo2["response"])

    df["Age"] = demo2["age"]
    df["Ethnicity"] = demo2["ethnicity"]

    # Psychopathology ----------------------------------------------------
    demo3 = data[data["screen"] == "demographics_disorders"].iloc[0]
    demo3 = json.loads(demo3["response"])

    df["Medical_Diagnostic"] = "; ".join(demo3["disorder_diagnostic"])
    df["Medical_Treatment"] = "; ".join(demo3["disorder_treatment"])

    # Questionnaires =====================================================

    # Questionnaire Order ------------------------------------------------
    # Select all screens start _with 'questionnaire'
    order = list(data[data["screen"].str.startswith("questionnaire")]["screen"])

    # PHQ4 ---------------------------------------------------------------
    phq4 = data[data["screen"] == "questionnaire_phq4"].iloc[0]

    df["PHQ4_Condition"] = phq4["condition"]
    df["PHQ4_Duration"] = phq4["rt"]
    df["PHQ4_Order"] = order.index("questionnaire_phq4") + 1

    phq4 = json.loads(phq4["response"])
    for item in phq4:
        df[item] = phq4[item]
