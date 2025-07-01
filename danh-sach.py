from firebase_admin import credentials, db, initialize_app

cred = credentials.Certificate("face-5fdcb-firebase-adminsdk-wpc4f-104fd09bc3.json")
initialize_app(cred, {
    'databaseURL': "https://face-5fdcb-default-rtdb.firebaseio.com/"
})

students_ref = db.reference('Students')
students = students_ref.get()

for student_id, info in students.items():
    print(f"MSSV: {student_id}")
    print(f"  Tên: {info['name']}")
    print(f"  Ngành: {info['major']}")
    print(f"  Số lần điểm danh: {info['total_attendance']}")
    print(f"  Lần cuối: {info['last_attendance_time']}")
    print("------")
