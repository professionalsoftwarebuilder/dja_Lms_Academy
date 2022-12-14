import sys

#---------------------------------------------------------------------------#
# Generic                                                                   #
#---------------------------------------------------------------------------#



#---------------------------------------------------------------------------#
# Database                                                                  #
#---------------------------------------------------------------------------#
SECRET_DB_USER = "django"
SECRET_DB_PASSWORD = "123password"


#---------------------------------------------------------------------------#
# Email                                                                     #
#---------------------------------------------------------------------------#
SECRET_EMAIL_HOST = ''
SECRET_EMAIL_PORT = 587
SECRET_EMAIL_HOST_USER = ''
SECRET_EMAIL_HOST_PASSWORD = ''


#---------------------------------------------------------------------------#
# Application Specific Settings                                             #
#---------------------------------------------------------------------------#
# (Disable Ads when running Unit-Tests)
if 'test' in sys.argv:
    APPLICATION_HAS_ADVERTISMENT = False  # (DO NOT MODIFY)
else:
    APPLICATION_HAS_ADVERTISMENT = False  # (True = Yes I want advertisments)


APPLICATION_HAS_PUBLIC_ACCESS_TO_TEACHERS = True