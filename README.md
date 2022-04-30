
# Lms Manager

Simple project to manage Moodle LMS account made with Python Basic Object Oriented
# Feature

| Feature             | Available                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Get Profile Details | ✅ |
| Get Activity Task | ✅ |
| Get Course List| ✅ |
| Auto Save Cookies | ✅ |
| Auto Login with Cookies | ✅ |
| Add Telegram Notification | Coming Soon |
| Add CronJobs Automatic Message | Coming Soon |


# Installation

Git Clone this project

```bash
  cd lmsmanager
  pip install -r .\requirements.txt
```
    
# Usage/Examples
use Example.py

```Python
from src.LmsManager import *
try:
    lmsm = LmsManager(username="", password="")
    lmsm.Login()

    print("Get Profile Details : ")

    ProfileDetails = lmsm.get_profile()
    print(ProfileDetails)
    
except LoginError as e:
    print(e)

except GetActivityError as e:
    print(e)

```


## API Reference

#### Define Class Function

```Python
  lmsm = LmsManager(username="", password="")
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your Username Account |
| `password` | `string` | **Required**. Your Password Account |

#### Get Details Profile Current Login

```Python
  ProfileDetails = lmsm.get_profile()
```
#### Output
![GetProfile](https://i.ibb.co/7NWZGb3/image.png)

#### Get Activity Task

```Python
  GetActivityTask = lmsm.Get_activity(end_time=30)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `end_time` | `integer` | maximum date of assignment ( Default is 6 Days) |

#### Output
![GetActivity](https://i.ibb.co/GRjS3pV/image.png)

#### Get Course list 

```Python
  GetCourselist = lmsm.get_course()
```

#### Output
![GetCourse](https://i.ibb.co/jTLvLm2/image.png)

# Screenshot

![GetProfile](https://i.ibb.co/XtpW3gM/image.png)

# Support

For support, or have error email krisandromartinus@gmail.com

