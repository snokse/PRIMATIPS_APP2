    label_texts = [
        "NBR : "+str(countALL), "1", "X", "2", "PM", "B/SB", "TOTAL",
        "1 : ( " +str(search_entry_BET1.get())+")", countDic["count_1_1"] , countDic["count_1_X"], countDic["count_1_2"], countDic["count_1_PM"], countDic["count_1_BUT"], "Label 14",
        "X : ( " +str(search_entry_BETX.get())+")", countDic["count_X_1"] , countDic["count_X_X"], countDic["count_X_2"], countDic["count_X_PM"], countDic["count_X_BUT"], "Label 21",
        "2 : ( " +str(search_entry_BET2.get())+")", countDic["count_2_1"] , countDic["count_2_X"], countDic["count_2_2"], countDic["count_2_PM"], countDic["count_2_BUT"], "Label 28",
        "1X", countDic["count_1X_1"] , countDic["count_1X_X"], countDic["count_1X_2"], countDic["count_1X_PM"], countDic["count_1X_BUT"], countDic["count_1X"],
        "12", countDic["count_12_1"] , countDic["count_12_X"], countDic["count_12_2"], countDic["count_12_PM"], countDic["count_12_BUT"], countDic["count_12"],
        "X2", countDic["count_X2_1"] , countDic["count_X2_X"], countDic["count_X2_2"], countDic["count_X2_PM"], countDic["count_X2_BUT"], countDic["count_X2"],
        "1X2", countDic["count_1X2_1"] , countDic["count_1X2_X"], countDic["count_1X2_2"], countDic["count_1X2_PM"], countDic["count_1X2_BUT"], countDic["count_1X2"]
    ]


countListe = [
    "count_1_1", "count_1_X", "count_1_2", "count_1_PM", "count_1_BUT",
    "count_X_1", "count_X_X", "count_X_2", "count_X_PM", "count_X_BUT",
    "count_2_1", "count_2_X", "count_2_2", "count_2_PM", "count_2_BUT",
    "count_1X_1", "count_1X_X", "count_1X_2", "count_1X_PM", "count_1X_BUT",
    "count_12_1", "count_12_X", "count_12_2", "count_12_PM", "count_12_BUT",
    "count_X2_1", "count_X2_X", "count_X2_2", "count_X2_PM", "count_X2_BUT",
    "count_1X2_1", "count_1X2_X", "count_1X2_2", "count_1X2_PM", "count_1X2_BUT"
]

countDic = {}

for key in countListe:
    countDic[key] = 0

print(countDic)
