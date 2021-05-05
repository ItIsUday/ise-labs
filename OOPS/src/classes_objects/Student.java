package classes_objects;

class Student {

    String name, usn;
    Address address;

    Student(String name, String usn, Address address) {
        this.name = name;
        this.usn = usn;
        this.address = address;
    }

    @Override
    public String toString() {
        return "Student " + name + " with USN " + usn + " is at " + address;
    }
}
