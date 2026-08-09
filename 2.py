import app_data
from one import login

print(app_data.app_state["logged_in"])  # False

login()

print(app_data.app_state["logged_in"])  # True