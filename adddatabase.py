import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("face-5fdcb-firebase-adminsdk-wpc4f-104fd09bc3.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-5fdcb-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

    "20224489":
        {
            "name": "Tran Vuong Thinh",
            "major": "Student",
            "starting_year": 2025,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "20224472":
        {
            "name": "Ha Tuan Anh",
            "major": "Student",
            "starting_year": 2025,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-12-11 00:54:34"
        },
    "20224471":
        {
            "name": "Hoang Dinh Quoc An",
            "major": "Student",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-12-11 00:54:34"
        },

    "20224475":
        {
            "name": "Pham Tuan Canh",
            "major": "Student",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-12-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)