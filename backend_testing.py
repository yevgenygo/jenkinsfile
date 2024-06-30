import requests
import db_connector
from rest_requests import get_user,post_user

USER_ID = 5
USER_NAME = "test"


post_json, post_status = post_user(USER_ID,USER_NAME)
if post_status == 200:
    user_name_from_get, get_status = get_user(USER_ID)
    if user_name_from_get == USER_NAME:
        print("Test passed successfully - GET REST method showed the same user name that was sent by POST REST METHOD")
        print("Status of get rest request: " + str(get_status))
        print("Direct query for user name from DB: " + str(db_connector.get_user(USER_ID)))
    else:
        print("Status of get rest request" + str(get_status))
else:
    print("POST user failed:" + str(post_json))
