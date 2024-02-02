import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': "https://smartattendancesystem-845a2-default-rtdb.firebaseio.com/"})

ref = db.reference("Students")
data = {"AS2020925": {
    "name": "Tharindu",
    "department": "ICT",
    "gender": "M",
    "indexNo": "AS2020925",
    "year": 3,
    "total_attendance": 6,
    "last_attendance_time": "2024-01-05 00:08:03"
},
    "AS2020924": {
        "name": "Sandarenu",
        "department": "CS",
        "gender": "F",
        "indexNo": "AS2020924",
        "year": 4,
        "total_attendance": 2,
        "last_attendance_time": "2023-12-12 00:07:49"
    },
    "AS2020904": {
        "name": "Gayan",
        "department": "CHE",
        "gender": "M",
        "indexNo": "AS2020904",
        "year": 2,
        "total_attendance": 2,
        "last_attendance_time": "2023-12-15 00:05:49"
    }
}
for key, value in data.items():
    ref.child(key).set(value)
