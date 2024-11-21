Simple Python-Script to auto-login into Dormitory-Internet-Access after the automatic logout at 07:00.
Executed on Mac by using pmset to wake up from Hibernation at 07:00, caffeinate to stay awake for 2 mins to
be able to execute the script via cronjob.


Enter Credentials in yaml file:
'''
lock_key_user:
  email: email
  password: password
'''



