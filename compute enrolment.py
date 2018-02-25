def compute_enrolment(num):
    if isinstance(num, int):
        if len(str(num)) > 3:
            raise ValueError("The length of num should be less than 4")
        elif len(str(num)) == 3:
            enrolment_id = '0' + str(num)
        elif len(str(num)) == 2:
            enrolment_id = '00' + str(num)
        elif len(str(num)) == 1:
            enrolment_id = '000' + str(num)
    print(enrolment_id)