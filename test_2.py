import app_data


a = app_data.app_state["dict"]

a["a"]["b"]["c"] = 5
print(a)
print(app_data.app_state["dict"])
print(app_data.app_state["dict"]["a"]["b"]["c"])
