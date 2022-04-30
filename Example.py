from src.LmsManager import *

try:
    lmsm = LmsManager(username="", password="")
    lmsm.Login()

    print("Get Profile Details : ")

    ProfileDetails = lmsm.get_profile()
    print("Fullname : {full_name}\nEmail : {email}\nFirst Access : {first_access}\nLast Access : {last_access}\n"
          .format(full_name=ProfileDetails['full_name'], email=ProfileDetails['email'],
                  first_access=ProfileDetails['first_access'], last_access=ProfileDetails['last_access']))

    print("\n" * 2)

    print("Get Activity Task : ")

    for activity in lmsm.Get_activity(end_time=30):
        print("Lesson Name : {nama_pelajaran}".format(nama_pelajaran=activity['full_name']))

        print("Task Name : {nama_tugas}".format(nama_tugas=activity['name']))

        print("Deadline : {deadline_human} - {deadline_date}".format(
            deadline_human=humanize.naturalday(activity['deadline_timestamp']),
            deadline_date=activity['deadline']))

        print("\n" * 2)

    print("Get Course List : ")

    for course in lmsm.get_course():
        print("Course Name : {nama_course}".format(nama_course=course['full_name']))

except LoginError as e:
    print(e)

except GetActivityError as e:
    print(e)
