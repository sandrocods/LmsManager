
# Lms Manager

Simple project to manage Moodle LMS account made with Python Basic Object Oriented
# Feature

| Feature             | Available                                                                | Added At                                                                |
| ----------------- | ------------------------------------------------------------------ |------------------------------------------------------------------ |
| Get Profile Details | ✅ | Project Release|
| Get Activity Task | ✅ | Project Release|
| Get Course List| ✅ | Project Release|
| Add Telegram Notification | ✅ |05-04-2022|
| Add CronJobs Automatic Message | ✅ |05-04-2022|


# Installation

Git Clone this project

```bash
  cd lmsmanager
  pip install .\requirements.txt
```
    
# Usage/Examples
use Example.py

```Python
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

Example for Send Notification Telegram
```Python
try:
    lmsm = LmsManager(username="", password="")
    lmsm.Login()

    lmsm.ScheduleTask(
        bot_token="",
        chat_id="",
        time_exec=120
    )
    
except LoginError as e:
    print(e)

except GetActivityError as e:
    print(e)

```
## API Reference

#### Define python Function

```python
  lmsm = LmsManager(username="", password="")
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your Username Account |
| `password` | `string` | **Required**. Your Password Account |

#### Get Details Profile Current Login

```python
  ProfileDetails = lmsm.get_profile()
```
#### Output
![GetProfile](https://i.ibb.co/7NWZGb3/image.png)

#### Get Activity Task

```python
  lmsm.Get_activity(end_time=30)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `end_time` | `integer` | maximum date of assignment ( Default is 6 Days) |

#### Output
![GetActivity](https://i.ibb.co/GRjS3pV/image.png)

#### Get Course list 

```python
  lmsm.get_course()
```

#### Output
![GetCourse](https://i.ibb.co/jTLvLm2/image.png)

#### Send Notification to Telegram Message

```python
    lmsm.ScheduleTask(bot_token="", chat_id="", time_exec=120)
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `bot_token` | `string` | **Required**. Your Bot Token Key |
| `chat_id` | `string` | **Required**. Your Chat ID |
| `time_exec` | `integer` | How many seconds is executed ( Default is 10 second ) |

#### Output
![GetActivity](https://i.ibb.co/wdG5Mmc/image.png)

#### ❗️ Better to use at the end of all functions because it uses blocking scheduler
# Screenshot

![GetProfile](https://i.ibb.co/XtpW3gM/image.png)

# Support

For support, or have error email krisandromartinus@gmail.com

