# dsagroupproject.py
Student Management System
This project is a student management system developed in Python for CSCI 046: Data Structures and Algorithms at Claremont McKenna College (Spring 2025). The system demonstrates how multiple data structures—namely hash tables, linked lists, and arrays—can be used together to efficiently manage student records.

## Team Members
- Maria Navarro Gonzalez  
- Chris Kim  
- Roman Sycz  
- Daniel Wu  

## Project Overview

Managing student records efficiently becomes increasingly difficult as institutions grow. This project addresses that challenge by building a system that allows for fast insertions, deletions, lookups, and listing of students across different departments.

Key functionalities:
- Add, delete, and update student records
- Retrieve student data using student IDs
- Maintain department-specific linked lists, sorted by class year and student ID
- Mass upload student data
- View a complete list of students

## Technologies & Structures Used

- Python 3
- Hash Table (`dict`): O(1) lookup by student ID
- Linked List: Separate sorted list per department; O(n) insertion/removal
- Array/List: Used to compile and display all student records; O(n) access

## File Structure

- `dsagroupproject.py` – Core implementation of the system, including:
  - `Student` class (with validation)
  - `Node` and `DepartmentList` classes (linked list logic)
  - `StudentManagementSystem` class (manages full functionality)

## Academic References

This project was developed with reference to:

CSCI 046 Lectures on Linked Lists and Hash Tables:
- Ahmadnia, Benyamin. (2025, February 12). Linked List [Lecture Slides].
- Ahmadnia, Benyamin. (2025, April 9). Hashing (Dictionaries) [Lecture Slides].
(https://github.com/user-attachments/assets/9f8d1879-b6e8-499d-ad9a-8ad2aa311579)

- [GeeksforGeeks: Student Management System in Python](https://www.geeksforgeeks.org/student-management-system-in-python/)
- [ResearchGate: Implementing a Simple Hash Table for Student Records](https://www.researchgate.net/publication/382366177_Implementing_a_Simple_Hash_Table_for_Student_Records)

## Time Complexities

| Operation               | Data Structure     | Time Complexity |
|------------------------|--------------------|------------------|
| Lookup by Student ID   | Hash Table         | O(1)             |
| Insertion/Removal      | Linked List        | O(n)             |
| View All Students      | Array/List         | O(n)             |

## Future Improvements

- Add data persistence (file or database storage)
- Implement user authentication
- Develop a graphical or web-based user interface
- Enable filtering and searching by attributes (e.g., GPA, class year)
- Improve scalability for institutions with larger student bodies

## Demo

YouTube demo: [Watch Here](https://www.youtube.com/watch?v=3-X2f8QZuGU)

## License

This project is for academic and educational purposes only.
