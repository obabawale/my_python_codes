# This program computes CGPA for a student in 5 different subjects
# This program is designed by and remains the property of Adedeji Abioye - 08065402856
# Piration or copying any part of this code is prohibited by law
# ______________________________________________________________________________________________________________________________________
StdName1=  raw_input ("Enter the Name of the Student to compute the CGPA For :" )

Subject_Name1=  raw_input ("Enter the Name of 1st subject offered by the student " )
Subject_Name2=  raw_input ("Enter the Name of 2nd subject offered by the student " )
Subject_Name3=  raw_input ("Enter the Name of 3rd subject offered by the student " )
Subject_Name4=  raw_input ("Enter the Name of 4th subject offered by the student " )
Subject_Name5=  raw_input ("Enter the Name of 5th subject offered by the student " )
print "________________________________________________________________________________________________________________________________"

CA_Score_Sub1= input ("Enter CA1 score for the student for the 1st subject ")
CA_Score_Sub2= input ("Enter CA2 score for the student for the 2nd subject ")
CA_Score_Sub3= input ("Enter CA3 score for the student for the 3rd subject ")
CA_Score_Sub4= input ("Enter CA4 score for the student for the 4th subject ")
CA_Score_Sub5= input ("Enter CA5 score for the student for the 5th subject ")
print "________________________________________________________________________________________________________________________________"

Exam_Score_Sub1= float(input ("Enter Exam score for the student for the 1st subject "))
Exam_Score_Sub2= float(input ("Enter Exam score for the student for the 2nd subject "))
Exam_Score_Sub3= float(input ("Enter Exam score for the student for the 3rd subject "))
Exam_Score_Sub4= float(input ("Enter Exam score for the student for the 4th subject "))
Exam_Score_Sub5= float(input ("Enter Exam score for the student for the 5th subject "))
print "________________________________________________________________________________________________________________________________"

if (CA_Score_Sub1) or (CA_Score_Sub2) or (CA_Score_Sub3) or (CA_Score_Sub4) or (CA_Score_Sub5) > 40:
    print "The CA score for any of the 5 subjects offered cannot be greater than 40 %"
print  "________________________________________________________________________________________________________________________________"

elif (CA_Score_Sub1) or (CA_Score_Sub2) or (CA_Score_Sub3) or (CA_Score_Sub4) or (CA_Score_Sub5) < 0:
    print "No CA Score is allowed to be negative below zero "
print "________________________________________________________________________________________________________________________________"
elif (CA_Score_Sub1) or (CA_Score_Sub2) or (CA_Score_Sub3) or (CA_Score_Sub4) or (CA_Score_Sub5) >= 40:
    print "Program may not proceed"
print "________________________________________________________________________________________________________________________________"
else:
    print "program proceeding"
print "________________________________________________________________________________________________________________________________"
    

if (Exam_Score_Sub1) or (Exam_Score_Sub2) or (Exam_Score_Sub3) or (Exam_Score_Sub4) or (Exam_Score_Sub5) > 100:
    print "A maximum percentage score is 100 percent and no more"
print "________________________________________________________________________________________________________________________________"
elif ((Exam_Score_Sub1) or (Exam_Score_Sub2) or (Exam_Score_Sub3) or (Exam_Score_Sub4) or (Exam_Score_Sub5)) < 0:
        print "A negative score is not allowed as exam score."
print "________________________________________________________________________________________________________________________________"
elif ((Exam_Score_Sub1) or (Exam_Score_Sub2) or (Exam_Score_Sub3) or (Exam_Score_Sub4) or (Exam_Score_Sub5)) < 100:
    print "program proceeding"
print "________________________________________________________________________________________________________________________________"
else:
    print "Program in execution phase"
print "________________________________________________________________________________________________________________________________"
                
Credit_Unit_Sub1= int(input ("Enter the credit unit for the 1st subject "))
print "____________________________________________________________________"
Credit_Unit_Sub2= int(input ("Enter the credit unit for the 2nd subject "))
print "____________________________________________________________________"
Credit_Unit_Sub3= int(input ("Enter the credit unit for the 3rd subject "))
print "____________________________________________________________________"
Credit_Unit_Sub4= int(input ("Enter the credit unit for the 4th subject "))
print "____________________________________________________________________"
Credit_Unit_Sub5= int(input ("Enter the credit unit for the 5th subject "))
print "____________________________________________________________________"

if ((Credit_Unit_Sub1) or (Credit_Unit_Sub2) or (Credit_Unit_Sub3) or (Credit_Unit_Sub4) or (Credit_Unit_Sub5)) <=0:
    print "Credit should never be zero or less than zero"
print "____________________________________________________________________"
elif (Credit_Unit_Sub1) or (Credit_Unit_Sub2) or (Credit_Unit_Sub3) or (Credit_Unit_Sub4) or (Credit_Unit_Sub5) >0:
        print "Program is proceeding with execution in forward direction"
print "____________________________________________________________________"
else:
    print "Program still running in forward direction"
print "____________________________________________________________________"
Total_Score_Sub1= CA_Score_Sub1 + Exam_Score_Sub1
Total_Score_Sub2= CA_Score_Sub2 + Exam_Score_Sub2
Total_Score_Sub3= CA_Score_Sub3 + Exam_Score_Sub3
Total_Score_Sub4= CA_Score_Sub4 + Exam_Score_Sub4
Total_Score_Sub5= CA_Score_Sub5 + Exam_Score_Sub5

if  Total_Score_Sub1 >=100:
    value1 = 5
elif Total_Score_Sub1 >=90:
        value1=4.5
elif Total_Score_Sub1 >=80:
            value1=4.0
elif Total_Score_Sub1 >=70:
                value1=3.5
elif Total_Score_Sub1 >=60:
                    value1=3.0
elif Total_Score_Sub1 >=50:
                        value1=2.5
elif Total_Score_Sub1>=40:
                            value1=2.0
elif Total_Score_Sub1 >=30:
                                value1=1.5
elif Total_Score_Sub1>=20:
                                    value1=1.0
elif Total_Score_Sub1>=10:
                                        value1=0.5
else:
    print "Re-examine what you are trying to do"

# ----------------------------------------------------------------------------------------------------


if  Total_Score_Sub2 >=100:
    value2 = 5
elif Total_Score_Sub2 >=90:
        value2=4.5
elif Total_Score_Sub2 >=80:
            value2=4.0
elif Total_Score_Sub2 >=70:
                value2=3.5
elif Total_Score_Sub2 >=60:
                    value2=3.0
elif Total_Score_Sub2 >=50:
                        value2=2.5
elif Total_Score_Sub2>=40:
                            value2=2.0
elif Total_Score_Sub2 >=30:
                                value2=1.5
elif Total_Score_Sub2>=20:
                                    value2=1.0
elif Total_Score_Sub2>=10:
                                        value2=0.5
else:
    print "Re-examine what you are trying to do"
print "____________________________________________________________________"
# --------------------------------------------------------------------------------------------------

if  Total_Score_Sub3 >=100:
    value3 = 5
elif Total_Score_Sub3 >=90:
        value3=4.5
elif Total_Score_Sub3 >=80:
            value3=4.0
elif Total_Score_Sub3 >=70:
                value3=3.5
elif Total_Score_Sub3 >=60:
                    value3=3.0
elif Total_Score_Sub3 >=50:
                        value3=2.5
elif Total_Score_Sub3>=40:
                            value3=2.0
elif Total_Score_Sub3 >=30:
                                value3=1.5
elif Total_Score_Sub3>=20:
                                    value3=1.0
elif Total_Score_Sub3>=10:
                                        value3=0.5
else:
    print "Re-examine what you are trying to do"
print "____________________________________________________________________"


# --------------------------------------------------------------------------------------------------

if  Total_Score_Sub4 >=100:
    value4 = 5
elif Total_Score_Sub4 >=90:
        value4=4.5
elif Total_Score_Sub4 >=80:
            value4=4.0
elif Total_Score_Sub4 >=70:
                value4=3.5
elif Total_Score_Sub4 >=60:
                    value4=3.0
elif Total_Score_Sub4 >=50:
                        value4=2.5
elif Total_Score_Sub4>=40:
                            value4=2.0
elif Total_Score_Sub4 >=30:
                                value4=1.5
elif Total_Score_Sub4>=20:
                                    value4=1.0
elif Total_Score_Sub4>=10:
                                        value4=0.5
else:
    print "Re-examine what you are trying to do"
print "____________________________________________________________________"

# --------------------------------------------------------------------------------------------------

if  Total_Score_Sub5 >=100:
    value5 = 5
elif Total_Score_Sub5 >=90:
        value5=4.5
elif Total_Score_Sub5 >=80:
            value5=4.0
elif Total_Score_Sub5 >=70:
                value5=3.5
elif Total_Score_Sub5 >=60:
                    value5=3.0
elif Total_Score_Sub5 >=50:
                        value5=2.5
elif Total_Score_Sub5>=40:
                            value5=2.0
elif Total_Score_Sub5 >=30:
                                value5=1.5
elif Total_Score_Sub5>=20:
                                    value5=1.0
elif Total_Score_Sub5>=10:
                                        value5=0.5
else:
    print "Re-examine what you are trying to do"
print "____________________________________________________________________"
# ---------------------------------------------------------------------------------------------------

TP4Sub1 = Credit_Unit_Sub1 * value1
TP4Sub2 = Credit_Unit_Sub2 * value2
TP4Sub3 = Credit_Unit_Sub3 * value3
TP4Sub4 = Credit_Unit_Sub4 * value4
TP4Sub5 = Credit_Unit_Sub5 * value5

TCU4all5S = Credit_Unit_Sub1 + Credit_Unit_Sub2 + Credit_Unit_Sub3 + Credit_Unit_Sub4 + Credit_Unit_Sub5

CGPAVal = TP4Sub1 + TP4Sub2 + TP4Sub3 + TP4Sub4 + TP4Sub5
RealCGPA = CGPAVal /TCU4all5S

# -------------------------------------------------------------------------------------------------------

print "The Name of the student is: ",                                       StdName1
print "                                                                                       "
print "The 1st Subject offered by the student is :",                        Subject_Name2
print "                                                                                       "
print "The 1st Subject offered by the student is :",                        Subject_Name3
print "                                                                                       "
print "The 1st Subject offered by the student is :",                        Subject_Name4
print "                                                                                       "
print "The 1st Subject offered by the student is :",                        Subject_Name5
print "                                                                                       "

print "The total credit unit for all the 5 subjects earned is :",           TCU4all5S
print "                                                                                       "
print "The CGPA Value for the student is :",                                RealCGPA
