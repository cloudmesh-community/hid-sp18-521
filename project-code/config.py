mysql_user = 'IUuser'
mysql_user_password = 'Password123'

'''

pseudo code suggested by gregor

if there is no file at ~/.cloudmesh/tbd-config.yaml
   copy the file there from etc
   
read in the yaml
changed = false
if passwd == TBD
   get a new password
   changed = true
if username == TBD 
   get a new username
   changed = true
if changed:
   write the yaml file back to  ~/.cloudmesh/tbd-config.yaml

'''
