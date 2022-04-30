import re
import json
import requests
import humanize
from src.Exception import *
from os.path import exists
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

humanize.i18n.activate("id_ID")
endPoint = "https://lms.ittelkom-pwt.ac.id/"


class LmsManager:

    def __init__(self, username, password):
        self.id_user = None
        self.headers = None
        self.login_name = None
        self.sesskey = None
        self.moodle_session = None
        self.username = username
        self.password = password

        if not (self.username and self.password):
            raise LoginError(self.username, self.password)

        if not exists("./Cookie/user_cookie.json"):
            with open("./Cookie/user_cookie.json", "w") as save:
                save.write(
                    json.dumps(
                        {
                            "username": self.username,
                            "password": self.password
                        }, indent=2)
                )
            LmsManager.Login(self)

    def Save_cookie(self):
        with open("./Cookie/user_cookie.json", "w") as save:
            save.write(
                json.dumps(
                    {
                        "username": self.username,
                        "login_name": self.login_name,
                        "sesskey": self.sesskey,
                        "moodle_session": self.moodle_session,
                        "id_user": self.id_user
                    }, indent=5)
            )

    def check_cookie(self):
        if exists("./Cookie/user_cookie.json"):
            with open('./Cookie/user_cookie.json', 'r') as openfile:
                json_object = json.load(openfile)

                self.moodle_session = json_object['moodle_session']

                headers = {
                    "Host": "lms.ittelkom-pwt.ac.id",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Origin": "https://lms.ittelkom-pwt.ac.id",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Referer": "https://lms.ittelkom-pwt.ac.id/",
                    "Cookie": f"MoodleSession={self.moodle_session}"
                }
                check_active_user = requests.get(url=endPoint + "my/", headers=headers)
                if "Forgotten" in check_active_user.text:
                    raise CookieExpire
                else:
                    pass

    def __process_login(self):
        get_login = requests.get(url=endPoint)
        login_token = \
            re.findall(pattern='<input type="hidden" name="logintoken" value="(.*?)" />',
                       string=get_login.text)[0]
        headers = {
            "Host": "lms.ittelkom-pwt.ac.id",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://lms.ittelkom-pwt.ac.id",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "https://lms.ittelkom-pwt.ac.id/",
            "Cookie": f"MoodleSession={get_login.cookies.get_dict()['MoodleSession']}"
        }
        login = requests.post(url=endPoint + "login/index.php",
                              data=f"logintoken={login_token}&username={self.username}&password={self.password}",
                              headers=headers,
                              allow_redirects=False
                              )
        if not login.cookies.get_dict():
            raise LoginError(self.username, self.password)
        else:
            del headers['Cookie']
            headers['Cookie'] = 'MoodleSession=' + login.cookies.get_dict()['MoodleSession']

            push_session = requests.get(url=login.headers['Location'], headers=headers,
                                        allow_redirects=False)

            main_dashbord = requests.get(url=push_session.headers['Location'], headers=headers)
            try:
                self.moodle_session = login.cookies.get_dict()['MoodleSession']
                self.sesskey = re.findall(
                                pattern='<input type="hidden" name="sesskey" value="(.*?)">',
                                string=main_dashbord.text)[0]
                self.login_name = re.findall(
                                pattern='<span class="usertext mr-1">(.*?)</span>',
                                string=main_dashbord.text)[0]

                self.headers = headers
                self.id_user = re.findall(pattern="testsession=(\d+)", string=login.headers['Location'])[0]
                self.Save_cookie()
            except IndexError:
                raise LoginError(self.username, self.password)

    def Login(self):
        """
        The above function is a function to login to the moodle website.
        :return: The return value is a dictionary with the following keys:
            error: Boolean value, True if there is an error, False if there is no error.
            login_name: String value, the name of the user who logged in.
            sesskey: String value, the session key of the user who logged in.
            moodle_session: String value, the
        """

        if exists("./Cookie/user_cookie.json"):
            with open('./Cookie/user_cookie.json', 'r') as openfile:
                json_object = json.load(openfile)

                try:
                    self.moodle_session = json_object['moodle_session']
                    self.sesskey = json_object['sesskey']
                    self.headers = {
                        "Host": "lms.ittelkom-pwt.ac.id",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "1",
                        "Origin": "https://lms.ittelkom-pwt.ac.id",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Referer": "https://lms.ittelkom-pwt.ac.id/",
                        "Cookie": f"MoodleSession={self.moodle_session}"
                    }

                    try:
                        self.check_cookie()
                    except CookieExpire:
                        self.__process_login()

                except KeyError:
                    self.__process_login()
        else:
            with open('./Cookie/user_cookie.json', 'r') as openfile:
                json_object = json.load(openfile)
            self.username = json_object['username']
            self.password = json_object['password']

            LmsManager.__process_login(self)

    def Get_activity(self, end_time=6):
        """
        The above function is used to get the activity of the user.
        :return: A list of dictionaries.
        """

        try:
            self.check_cookie()
        except CookieExpire:
            raise CookieExpire
        finally:
            data_activity = []
            current_ts = datetime.now()
            end_ts = current_ts + timedelta(days=end_time)

            get_activity = requests.post(
                url=endPoint + f"lib/ajax/service.php?sesskey={self.sesskey}&info=core_calendar_get_action_events_by_timesort",
                data='[{"index":0,"methodname":"core_calendar_get_action_events_by_timesort","args":{"limitnum":26,"timesortfrom":' + str(current_ts.timestamp()).split('.')[0] + ',"timesortto":' + str(end_ts.timestamp()).split('.')[0] + ',"limittononsuspendedevents":true}}]',
                headers=self.headers
            )

            json_decode = get_activity.json()
            if not json_decode[0]['error']:
                for data in json_decode[0]['data']['events']:
                    data_activity.append({
                        'full_name': data['course']['fullnamedisplay'],
                        'name': data['name'],
                        'deadline': datetime.fromtimestamp(data['timeusermidnight']).strftime('%d-%m-%y %H:%M:%S'),
                        'deadline_timestamp': datetime.fromtimestamp(data['timeusermidnight'])
                    })
                return data_activity
            else:
                raise GetActivityError

    def get_course(self):
        try:
            self.check_cookie()
        except CookieExpire:
            raise CookieExpire
        finally:
            course_list = []
            get_course = requests.post(
                url=endPoint + f"lib/ajax/service.php?sesskey={self.sesskey}&info=core_course_get_enrolled_courses_by_timeline_classification",
                data='[{"index":0,"methodname":"core_course_get_enrolled_courses_by_timeline_classification","args":{"offset":0,"limit":0,"classification":"all","sort":"shortname","customfieldname":"","customfieldvalue":""}}]',
                headers=self.headers
            )

            json_decode = get_course.json()
            if not json_decode[0]['error']:
                for data in json_decode[0]['data']['courses']:
                    course_list.append({
                        'full_name': data['fullnamedisplay'],
                    })
                return course_list
            else:
                raise GetActivityError

    def get_profile(self):
        """
        It gets the profile of the user and returns a dictionary with the full name, email, first access and last access of
        the user
        :return: A dictionary with the user's full name, email, first access, and last access.
        """
        try:
            self.check_cookie()
        except CookieExpire:
            raise CookieExpire
        finally:
            get_profile = requests.get(url=endPoint + f"user/profile.php?id={self.id_user}", headers=self.headers)
            parse = BeautifulSoup(get_profile.text, 'html.parser')
            if not parse.find('h1').text:
                raise GetActivityError
            else:
                return {
                    'full_name': parse.find('h1').text,
                    'email': parse.find('dd').findNext('a').text,
                    'first_access': parse.find('li', {"class": "contentnode"}).findNext('dt',
                                                                                        text='First access to site').findNext(
                        'dd').text,
                    'last_access': parse.find('li', {"class": "contentnode"}).findNext('dt',
                                                                                       text='Last access to site').findNext(
                        'dd').text
                }
