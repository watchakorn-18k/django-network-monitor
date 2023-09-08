<div align="center">

# Django Network Monitor (Thai language)

Test run on raspberry pi 4 (4GB)

![](https://media.discordapp.net/attachments/372372440334073859/1149791658808967330/Screenshot_2023-09-09_023507.png?width=1440&height=442)

</div>

## User

Admin

```
username = pi
password = 12345678
```

## Installation

```
git clone https://github.com/watchakorn-18k/django-network-monitor
cd django-network-monitor
cd wk18k
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Code that is unique from other codes

On line 127 of the settings.py file, the shared login state session is added.

```
127    SESSION_ENGINE = 'django.contrib.sessions.backends.db'
```

Add static file

```
129    import os
130    STATIC_URL = '/static/'
131    STATICFILES_DIRS = [
132        os.path.join(BASE_DIR, 'static'),
133    ]
```

## Start

- Go to http://127.0.0.1:8000/

## Example

<div align="center">
<table>
   <tbody>
     <tr>
       <td>
       
![home](https://cdn.discordapp.com/attachments/372372440334073859/1149776671189241999/image.png)
       </td>
       <td>
       
![admin](https://cdn.discordapp.com/attachments/372372440334073859/1149776898344362024/image.png)</td>
     </tr>
     <tr>
<td>

![admin](https://cdn.discordapp.com/attachments/372372440334073859/1149777218109706310/image.png)</td>

<td>

![login](https://media.discordapp.net/attachments/372372440334073859/1149777313303638067/image.png)</td>

  </tbody>
</table>

Copyright © 2023 All right reserved by https://github.com/watchakorn-18k/django-network-monitor/

</div>
