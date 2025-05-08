from dsagroupproject import StudentManagementSystem, Student
import time

def run_tests():
    print("Starting test suite...")
    
    # Add a valid student
    sms = StudentManagementSystem()
    assert sms.add_student(1, "Alice", 3.5, "Sophomore", "CS", "Mathematical Studies") == True
    print("Added valid student")

    # Retrieve student by ID
    student = sms.get_student_by_id(1)
    assert student is not None and student.name == "Alice"
    print("Retrieved student by ID")

    # Delete student
    assert sms.delete_student(1) == True
    print("Deleted student by ID")

    # List all students (should be empty)
    assert sms.list_all_students() == []
    print("No students after deletion")

    # Validation Errors
    try:
        Student(-1, "Bob", 3.0, "Junior", "History", "Humanities")
    except ValueError:
        print("Invalid student_id")

    try:
        Student(2, "", 3.0, "Junior", "History", "Humanities")
    except ValueError:
        print("Empty name")

    try:
        Student(3, "Charlie", 4.5, "Senior", "Chemistry", "Natural Sciences")
    except ValueError:
        print("Invalid GPA")

    try:
        Student(4, "Dana", 3.0, "Graduate", "Psychology", "Social Sciences")
    except ValueError:
        print("Invalid class year")

    try:
        Student(5, "Eve", 3.0, "Freshman", "", "Social Sciences")
    except ValueError:
        print("Empty major")

    try:
        Student(6, "Frank", 3.0, "Junior", "Math", "Engineering")
    except ValueError:
        print("Invalid department")

    # Duplicate Student ID
    sms = StudentManagementSystem()
    sms.add_student(7, "Grace", 3.6, "Senior", "Physics", "Natural Sciences")
    assert sms.add_student(7, "Hank", 3.1, "Junior", "Physics", "Natural Sciences") == False
    print("Duplicate student ID rejected")

    # GPA Boundaries
    assert sms.add_student(8, "Ivy", 0.0, "Freshman", "Biology", "Natural Sciences") == True
    assert sms.add_student(9, "Jake", 4.0, "Senior", "Chemistry", "Natural Sciences") == True
    print("GPA boundaries accepted (0.0 and 4.0)")

    # Department Sorting Order
    sms.add_student(10, "Zane", 3.2, "Freshman", "CS", "Mathematical Studies")
    sms.add_student(11, "Yara", 3.2, "Senior", "CS", "Mathematical Studies")
    sms.add_student(12, "Xander", 3.2, "Senior", "CS", "Mathematical Studies")
    sms.get_department_students("Mathematical Studies")  # Should print Xander, Yara, Zane

    # Remove Nonexistent Student
    assert sms.delete_student(9999) == False
    print("Removing nonexistent student returns False")

    # Update with Invalid Department
    assert sms.update_student(10, department="Engineering") == False
    print("Update with invalid department fails")

    # Test small CSV upload
    print("\nTesting small CSV upload (4 students)...")
    start_time = time.time()
    sms = StudentManagementSystem()
    sms.mass_upload("test_students.csv")
    small_csv_time = time.time() - start_time
    print(f"Small CSV upload completed in {small_csv_time:.2f} seconds")

    # Test large CSV upload
    print("\nTesting large CSV upload (80 students)...")
    start_time = time.time()
    sms = StudentManagementSystem()
    sms.mass_upload("large_test_students.csv")
    large_csv_time = time.time() - start_time
    print(f"Large CSV upload completed in {large_csv_time:.2f} seconds")

    # Verify department sorting with large dataset
    print("\nVerifying department sorting with large dataset...")
    departments = ["Humanities", "Natural Sciences", "Mathematical Studies", "Social Sciences"]
    for dept in departments:
        print(f"\nChecking {dept} department:")
        sms.get_department_students(dept)

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    run_tests() 