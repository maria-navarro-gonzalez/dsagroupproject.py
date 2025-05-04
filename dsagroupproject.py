import pandas as pd
class Node:
    def __init__(self, student_data):
        self.student_data = student_data
        self.next = None

class Student:
    def __init__(self, student_id, name, gpa, class_year, major, department):
        # Validate student_id
        if not isinstance(student_id, int) or student_id <= 0:
            raise ValueError("Student ID must be a positive integer")

        # Validate name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        # Validate GPA
        if not isinstance(gpa, (int, float)) or gpa < 0 or gpa > 4.0:
            raise ValueError("GPA must be a number between 0 and 4.0")

        # Validate class_year
        valid_years = ["Freshman", "Sophomore", "Junior", "Senior"]
        if class_year not in valid_years:
            raise ValueError(f"Class year must be one of: {', '.join(valid_years)}")

        # Validate major
        if not isinstance(major, str) or not major.strip():
            raise ValueError("Major must be a non-empty string")

        # Validate department
        valid_departments = ["Humanities", "Natural Sciences", "Mathematical Studies", "Social Sciences"]
        if department not in valid_departments:
            raise ValueError(f"Department must be one of: {', '.join(valid_departments)}")

        self.student_id = student_id
        self.name = name
        self.gpa = gpa
        self.class_year = class_year
        self.major = major
        self.department = department

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Year: {self.class_year}, Major: {self.major}, Department: {self.department}, GPA: {self.gpa}"

class DepartmentList:
    def __init__(self, department_name):
        self.department_name = department_name
        self.head = None
    
    def insert_sorted(self, new_student):
        new_node = Node(new_student)
        
        # Convert class year to numeric value for comparison
        year_values = {"Senior": 4, "Junior": 3, "Sophomore": 2, "Freshman": 1}
        new_year_value = year_values[new_student.class_year]
        
        # If list is empty or new student should be at head
        if not self.head or (year_values[self.head.student_data.class_year] < new_year_value or 
                            (year_values[self.head.student_data.class_year] == new_year_value and 
                             self.head.student_data.student_id > new_student.student_id)):
            new_node.next = self.head
            self.head = new_node
            return
        
        # Otherwise, find the correct position
        current = self.head
        while current.next and (year_values[current.next.student_data.class_year] > new_year_value or 
                              (year_values[current.next.student_data.class_year] == new_year_value and 
                               current.next.student_data.student_id < new_student.student_id)):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
    
    def remove_student(self, student_id):
        if not self.head:
            return False
        
        if self.head.student_data.student_id == student_id:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.student_data.student_id == student_id:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def get_student_list(self):
        result = []
        current = self.head
        while current:
            student = current.student_data
            result.append({
                'id': student.student_id,
                'name': student.name,
                'year': student.class_year
            })
            current = current.next

        # Print the formatted list
        print(f"\n{self.department_name} Department Students:")
        if result:
            for student in result:
                print(f"ID: {student['id']}, Name: {student['name']}, Year: {student['year']}")
        else:
            print("No students in this department.")
            
        return result

class StudentManagementSystem:
    def __init__(self):
        self.hash_table = {}  # Hash table for O(1) lookups by student ID
        self.student_array = []  # Array to store all students
        
        # Initialize department lists
        self.department_lists = {
            "Humanities": DepartmentList("Humanities"),
            "Natural Sciences": DepartmentList("Natural Sciences"),
            "Mathematical Studies": DepartmentList("Mathematical Studies"),
            "Social Sciences": DepartmentList("Social Sciences")
        }

    def add_student(self, student_id, name, gpa, class_year, major, department):
        """Add a new student to the system"""
        try:
            # Check if student ID already exists
            if student_id in self.hash_table:
                return False
            
            # Create new student object
            new_student = Student(student_id, name, gpa, class_year, major, department)
            
            # Add to hash table
            self.hash_table[student_id] = new_student
            
            # Add to array
            self.student_array.append(new_student)
            
            # Add to appropriate department list
            self.department_lists[department].insert_sorted(new_student)
            
            return True
        except ValueError as e:
            print(f"Error in adding student: {e}")
            return False

    def get_student_by_id(self, student_id):
        """Retrieve student information using student ID"""
        return self.hash_table.get(student_id)

    def delete_student(self, student_id):
        """Delete a student from the system"""
        if student_id not in self.hash_table:
            return False

        # Get student info before removal
        student = self.hash_table[student_id]
        
        # Remove from hash table
        del self.hash_table[student_id]
        
        # Remove from array
        self.student_array = [s for s in self.student_array if s.student_id != student_id]
        
        # Remove from department list
        self.department_lists[student.department].remove_student(student_id)
        
        return True

    def update_student(self, student_id, name=None, gpa=None, class_year=None, major=None, department=None):
        """Update student information"""
        student = self.hash_table.get(student_id)
        if not student:
            return False
        
        old_department = student.department

        # Update student information
        if name:
            student.name = name
        if gpa is not None:
            student.gpa = gpa
        if class_year:
            student.class_year = class_year
        if major:
            student.major = major
        if department:
            if department not in self.department_lists:
                return False
            student.department = department
        
        # If department changed or class year changed, reinsert into correct department list
        if department or class_year:
            self.department_lists[old_department].remove_student(student_id)
            self.department_lists[student.department].insert_sorted(student)
        
        return True

    def list_all_students(self):
        """List all students using the array"""
        print("\n=== Complete Student List ===")
        if self.student_array:
            for student in self.student_array:
                print(student)
        else:
            print("No students in the system.")
        return self.student_array

    def get_department_students(self, department):
        """Get sorted list of students in a department"""
        if department not in self.department_lists:
            return None
        return self.department_lists[department].get_student_list()

    import pandas as pd

    def mass_upload(self, csv_file_path):
        """
        Mass upload multiple students to the system from a CSV file.

        Args:
            csv_file_path: String path to the CSV file.
        """
        successful_uploads = 0
        failed_uploads = 0
        
        try:
            df = pd.read_csv(csv_file_path)
            
            for index, row in df.iterrows():
                success = self.add_student(
                    student_id=row['student_id'],
                    name=row['name'],
                    gpa=row['gpa'],
                    class_year=row['class_year'],
                    major=row['major'],
                    department=row['department']
                )
                
                if success:
                    successful_uploads += 1
                else:
                    failed_uploads += 1

            print(f"Successfully uploaded {successful_uploads} students to the database.")
            if failed_uploads > 0:
                print(f"Failed to upload {failed_uploads} students to the database.")

        except Exception as e:
            print(f"An error occurred during CSV upload: {e}")


# Example usage
def main():
    sms = StudentManagementSystem()
    
    # Add sample students
    sms.add_student(1101, "John Doe", 3.8, "Senior", "Computer Science", "Mathematical Studies")
    sms.add_student(1102, "Jane Smith", 3.9, "Junior", "Mathematics", "Mathematical Studies")

    sms.mass_upload("C:/Users/RomanSycz/Downloads/students.csv")
    
    # Print students by department (using linked list implementation)
    print("\n=== Department-wise Student List (Linked List Implementation) ===")
    departments = ["Humanities", "Natural Sciences", "Mathematical Studies", "Social Sciences"]
    for dept in departments:
        sms.get_department_students(dept)
    
    # Test updates
    print("\nUpdating student 1002 from Junior to Senior...")
    sms.update_student(1002, class_year="Senior")
    
    print("\nMathematical Studies Department after update:")
    sms.get_department_students("Mathematical Studies")

    # Test array implementation
    sms.list_all_students()

if __name__ == "__main__":
    main()
