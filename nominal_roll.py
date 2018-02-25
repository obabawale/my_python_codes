import csv
from datetime import datetime
path = "C:\\Users\\Olapade\\Desktop\\hr_nhrc\\employees_nominal_roll.csv"
file = open(path, newline='')
reader = csv.reader(file, delimiter=';')
header = next(reader)
data = []

#format each row according to their data types
for row in reader:

	myid = int(row[0]) # for the id field
	myaddress_id = int(row[1])	# for the address id field
	create_date	= datetime.strptime(row[2], '%m/%d/%y %I:%M %p')
	ssnid = row[3]
	coach_id = int(row[4])	
	message_last_post = datetime.strptime(row[5], '%m/%d/%y %I:%M %p')
	color = int(row[6])
	marital	= row[7]
	identification_id = str(row[7])
	bank_account_id	= int(row[8])
	job_id	= int(row[9])
	parent_id = int(row[10])
	work_phone	= row[11]
	resource_id	= int(row[12])
	country_id	= int(row[13])
	department_id = int(row[14])
	mobile_phone = row[15]
	create_uid	= int(row[16])
	birthday = datetime.strptime(row[17], '%m/%d/%y %I:%M %p')
	write_date	= datetime.strptime(row[18], '%m/%d/%y %I:%M %p')
	sinid = int(row[19])
	write_uid = int(row[20])
	work_email = row[21]
	work_location = row[22]
	gender = row[23]
	notes = row[24]
	address_home_id	= int(row[25])
	passport_id	= row[26]
	name_related = row[27]
	manager	= bool(row[28])
	children = int(row[29])
	medic_exam	= datetime.strptime(row[30], '%m/%d/%y %I:%M %p')
	vehicle	= row[31]
	place_of_birth = row[32]
	vehicle_distance = int(row[33])	
	bvn	= int(row[34])
	domicile = row[35]
	spouse_nationality = row[36]	
	languages_spoken = row[37]
	fileno = row[38]
	first_appointment_date = datetime.strptime(row[39], '%m/%d/%y %I:%M %p')
	designation	= row[40]
	full_resi_address = row[41]
	name_of_spouse = row[42]
	date_retirement	= datetime.strptime(row[43], '%m/%d/%y %I:%M %p')
	pensionno = row[44]
	present_appointment_date = datetime.strptime(row[45], '%m/%d/%y %I:%M %p')	
	village	= row[46]
	appointment_terms = row[47]
	pfa = int(row[48])
	pfc	= int(row[49])
	state_id = int(row[50])
	type_of_appointment	= row[51]
	department = int(row[52])
	lga_id = int(row[53])
	remarks	= row[54]
	salary_grade_level = row[55]
	stateoforigin = int(row[56])
	nationality = int(row[57])

    data.append([myid, healthdecisions, haveacar, create_date, house, ethnic, write_uid, runningwater, areyoumarried, occupation, ifmale, create_uid, educationlevel, firstsex,howlong, electricity, visitdate, mattress, other, iffemale, income, howlong2geda, deadchild, wantmore, resgender, livingchild, write_date, peopleinthehouse,concrete_or_cement, refrigerator, knowhowlong, roomsinthehouse, television, mobilephone, howmanyliving, noofdrink, goout, livetogether, marriedto, partner_id, sceening_id,dateofbirth])
    
    print(row)
file.close()