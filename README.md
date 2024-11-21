Simple Python-Script to auto-login into Dormitory-Internet-Access after the automatic logout at 07:00.
Executed on Mac by using pmset to wake up from Hibernation at 07:00, caffeinate to stay awake for 2 mins to
be able to execute the script via cronjob.


Enter Credentials in yaml file:
```
lock_key_user:
  email: email
  password: password
```

Use pmset in Terminal to schedule a wakeup everyday at 07:00:
```
sudo pmset repeat wake MTWRFSU 07:00:00
```

Write cronjob with execution for caffeinate & this script

```
crontab -e
```

Enter the following with your path:
```
0 7 * * * pgrep caffeinate -t 120
0 7 * * * ~/.venv/bin/python ~/LockKeyLoginAuto.py
```

Use ```:WQ``` to safe and quit the Vim-Editor.

You can check if the job is installed via:
```
crontab -l
```






