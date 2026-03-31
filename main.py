# from operations import *

# while True:
#     print("\n1. Add Student")
#     print("2. View Students")
#     print("3. Update Student")
#     print("4. Delete Student")
#     print("5. Search Student")
#     print("6. Topper")
#     print("7. Average Marks")
#     print("8. High Scorers")
#     print("9. Import CSV")
#     print("10. Export CSV")
#     print("11. Exit")

#     choice = input("Enter choice: ")

#     if choice == "1":
#         name = input("Enter name: ")
#         age = int(input("Enter age: "))
#         course = input("Enter course: ")
#         marks = int(input("Enter marks: "))
#         add_student(name, age, course, marks)

#     elif choice == "2":
#         view_students()

#     elif choice == "3":
#         student_id = int(input("Enter ID to update: "))
#         name = input("Enter new name: ")
#         age = int(input("Enter new age: "))
#         course = input("Enter new course: ")
#         marks = int(input("Enter new marks: "))
#         update_student(student_id, name, age, course, marks)

#     elif choice == "4":
#         student_id = int(input("Enter ID to delete: "))
#         delete_student(student_id)

#     elif choice == "5":
#         name = input("Enter name to search: ")
#         search_student(name)

#     elif choice == "6":
#         get_topper()

#     elif choice == "7":
#         get_average_marks()

#     elif choice == "8":
#         get_high_scorers()

#     elif choice == "9":
#         path = input("Enter CSV file path: ")
#         import_csv(path)

#     elif choice == "10":
#         path = input("Enter file path to save: ")
#         export_csv(path)

#     elif choice == "11":
#         break