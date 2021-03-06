import csv
from datetime import datetime
path = "C:\\Users\\Olapade\\Desktop\\enrollment_demographics_nnewi_datamanager1.csv"
file = open(path, newline='')
reader = csv.reader(file, delimiter=';')
header = next(reader)
data = []

#format each row according to their data types
for row in reader:    
    
    myid = (row[0])
    healthdecisions = str(row[1])
    haveacar = str(row[2])
    create_date = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S.%f")
    house = str(row[4])
    ethnic = str(row[5])
    write_uid = int(row[6])
    runningwater = str(row[7])
    areyoumarried = str(row[8])
    occupation = str(row[9])
    ifmale = str(row[10])
    create_uid = int(row[11])
    educationlevel = str(row[12])
    firstsex = datetime.strptime(row[13], "%Y-%m-%d")
    howlong = str(row[14])
    visitdate = datetime.strptime(row[15], "%Y-%m-%d")
    electricity = str(row[16])
    mattress = str(row[17])
    other = str(row[18])
    iffemale = str(row[19])
    income = str(row[20])
    howlong2geda = str(row[21])
    deadchild = str(row[22])
    wantmore = str(row[23])
    resgender = str(row[24])
    livingchild = str(row[25])
    write_date = datetime.strptime(row[26], "%Y-%m-%d %H:%M:%S.%f")
    peopleinthehouse = str(row[27])
    concrete_or_cement = str(row[28])
    refrigerator = str(row[29])
    knowhowlong = datetime.strptime(row[30], "%Y-%m-%d")
    roomsinthehouse = str(row[31])
    television = str(row[32])
    mobilephone = str(row[33])
    howmanyliving = str(row[34])
    noofdrink = str(row[35])
    goout = str(row[36])
    livetogether = str(row[37])
    marriedto = str(row[38])
    partner_id = int(row[39])
    sceening_id = str(row[40])
    dateofbirth = datetime.strptime(row[41], "%Y-%m-%d")
        
    data.append([myid, healthdecisions, haveacar, create_date, house, ethnic, write_uid, runningwater, areyoumarried, occupation, ifmale, create_uid, educationlevel, firstsex,howlong, electricity, visitdate, mattress, other, iffemale, income, howlong2geda, deadchild, wantmore, resgender, livingchild, write_date, peopleinthehouse,concrete_or_cement, refrigerator, knowhowlong, roomsinthehouse, television, mobilephone, howmanyliving, noofdrink, goout, livetogether, marriedto, partner_id, sceening_id,dateofbirth])
    
    print(row)
file.close()