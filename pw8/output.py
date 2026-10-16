# output.py
import csv
import pickle
import gzip
import threading

# --- LƯU FILE BẰNG THREAD CHẠY ẨN (PW8 REQUIREMENT) ---
def _save_pickle_gz(filename, data):
    """Hàm chạy ẩn trong Thread để nén và ghi đè file .pkl.gz"""
    try:
        with gzip.open(filename, "wb") as f:
            pickle.dump(data, f)
        print(f"[Background Thread] Đã lưu thành công: {filename}")
    except Exception as e:
        print(f"[Thread Error] Lỗi khi lưu {filename}: {e}")

def save_all_data_async(students, courses, marks):
    """Khởi tạo các luồng chạy ẩn lưu students, courses, marks đồng thời"""
    t1 = threading.Thread(target=_save_pickle_gz, args=("students.pkl.gz", students))
    t2 = threading.Thread(target=_save_pickle_gz, args=("courses.pkl.gz", courses))
    t3 = threading.Thread(target=_save_pickle_gz, args=("marks.pkl.gz", marks))

    # Kích hoạt các thread chạy song song nền
    t1.start()
    t2.start()
    t3.start()


# --- HIỂN THỊ DỮ LIỆU ---
def list_students(students):
    print("\n=== DANH SÁCH SINH VIÊN (SẮP XẾP THEO GPA) ===")
    for s in students:
        print(f"[Student] ID: {s.id():<10} | Name: {s.name():<20} | DoB: {s.dob():<12} | GPA: {s.gpa():.2f}")

def list_courses(courses):
    print("\n=== DANH SÁCH MÔN HỌC ===")
    for c in courses:
        print(f"[Course]  ID: {c.id():<10} | Name: {c.name():<20} | Credits: {c.credits()}")

def sort_students(students):
    return sorted(students, key=lambda s: s.gpa(), reverse=True)


# --- XUẤT FILE CSV ---
def export_students(students):
    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "DoB", "GPA"])
        for s in students:
            writer.writerow([s.id(), s.name(), s.dob(), s.gpa()])
    print("[CSV Export] Đã xuất students.csv")

def export_courses(courses):
    with open("courses.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Credits"])
        for c in courses:
            writer.writerow([c.id(), c.name(), c.credits()])
    print("[CSV Export] Đã xuất courses.csv")

def export_marks(students):
    with open("marks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Student_ID", "Course_ID", "Mark"])
        for s in students:
            for c_id, mark in s.marks().items():
                writer.writerow([s.id(), c_id, mark])
    print("[CSV Export] Đã xuất marks.csv")


# --- TRA CỨU SINH VIÊN ---
def query_students():
    q_id = input("\nNhập Mã sinh viên cần tra cứu (hoặc ấn Enter để bỏ qua): ").strip()
    if not q_id:
        return

    try:
        with gzip.open("students.pkl.gz", "rb") as f:
            students = pickle.load(f)
            for s in students:
                if s.id() == q_id:
                    print(f"\n--- KẾT QUẢ TRA CỨU ---")
                    print(f"ID: {s.id()} | Name: {s.name()} | DoB: {s.dob()} | GPA: {s.gpa()}")
                    print("Marks:", s.marks())
                    return
            print(f"Không tìm thấy sinh viên có ID '{q_id}'.")
    except Exception as e:
        print(f"Lỗi khi đọc file nén: {e}")