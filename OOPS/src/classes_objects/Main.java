package classes_objects;

import java.util.Scanner;

public class Main {
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        Student[] students = inputStudentLists();
        System.out.println();
        College[] colleges = inputCollegeList();
        System.out.println();
        Employee[] employees = inputEmployeesList();

        System.out.println("\nThe " + students.length + " students are: ");
        printArray(students);
        System.out.println("\nThe " + colleges.length + " college are: ");
        printArray(colleges);
        System.out.println("\nThe " + employees.length + " employees are: ");
        printArray(employees);
    }

    static Address inputAddress() {
        String streetNum, city, state, country;

        System.out.print("Street number: ");
        streetNum = in.nextLine();

        System.out.print("City: ");
        city = in.nextLine();

        System.out.print("State: ");
        state = in.nextLine();

        System.out.print("Country: ");
        country = in.nextLine();

        return new Address(streetNum, city, state, country);
    }

    static Student[] inputStudentLists() {
        int count;
        String name, usn;
        Address address;
        System.out.print("Enter the number of students: ");
        count = in.nextInt();
        in.nextLine(); // Consumes newline left-over

        Student[] students = new Student[count];
        for (int i = 0; i < count; i++) {
            System.out.println();
            System.out.println("Fill student " + (i + 1) + " details: ");

            System.out.print("Name: ");
            name = in.nextLine();

            System.out.print("USN: ");
            usn = in.nextLine();

            address = inputAddress();

            students[i] = new Student(name, usn, address);
        }

        return students;
    }

    static College[] inputCollegeList() {
        int count;
        String name;
        Address address;
        System.out.print("Enter the number of colleges: ");
        count = in.nextInt();
        in.nextLine(); // Consumes newline left-over

        College[] colleges = new College[count];
        for (int i = 0; i < count; i++) {
            System.out.println();
            System.out.println("Fill college " + (i + 1) + " details: ");

            System.out.print("Name: ");
            name = in.nextLine();

            address = inputAddress();

            colleges[i] = new College(name, address);
        }

        return colleges;
    }

    static Employee[] inputEmployeesList() {
        int count;
        String name, empId;
        Address address;
        System.out.print("Enter the number of employees: ");
        count = in.nextInt();
        in.nextLine(); // Consumes newline left-over

        Employee[] employees = new Employee[count];
        for (int i = 0; i < count; i++) {
            System.out.println();
            System.out.println("Fill employee " + (i + 1) + " details: ");

            System.out.print("Name: ");
            name = in.nextLine();

            System.out.print("EmpID: ");
            empId = in.nextLine();

            address = inputAddress();

            employees[i] = new Employee(name, empId, address);
        }

        return employees;
    }

    public static <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }
}

