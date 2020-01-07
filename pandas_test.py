import pandas

dataFrame = pandas.read_csv("report.csv")
# pandas.set_option('display.max_rows', None)
# pandas.set_option('display.max_columns', None)
# pandas.set_option('display.width', None)
# pandas.set_option('display.max_colwidth', -1)
file = open("eidList","r")
managerName = input("Enter Manager Name: ")
eidList = []
for eid in file.readlines():
    eidList.append(eid)

dataFrame.Name = dataFrame.Name.str.split("(",expand=True)

dataFrameEid=pandas.DataFrame(eidList,columns=["Eid"])

dataFrameEid = dataFrameEid["Eid"].fillna(0).astype(int)
NewDataFrame = dataFrame[["Eid","APAC","EMEA","WH - India"]].fillna(0).astype(int)
NewDataFrame.insert(1,"Name",dataFrame.Name)
intersection_dataframe = pandas.merge(dataFrameEid, NewDataFrame, how='inner', on='Eid')
intersection_dataframe.insert(2,"Name Manager",managerName)
#print (dataFrame[["Eid","APAC","EMEA","WH - India"]].fillna(0),"\n",dataFrameEid)

intersection_dataframe.to_csv("FinalReport.csv")

# for eid in eidList:
#     if eid in dataFrame.Eid:
#         print (eid)
#         print(dataFrame[["Eid","APAC","EMEA","WH - India"]].fillna(0))


# print(dataFrame[["Eid","APAC","EMEA","WH - India"]].fillna(0))
# for k,v in a.items():
#     print("{} : {}".format(k,v))

# print(dataFrame.fillna(0).to_dict())
# a = (dataFrame.fillna(0).to_dict())
