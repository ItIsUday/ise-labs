package classes_objects;

class Employee {

    String name, empId;
    Address address;

    Employee(String name, String empId, Address address) {
        this.name = name;
        this.empId = empId;
        this.address = address;
    }

    @Override
    public String toString() {
        return "Employee " + name + " with ID " + empId + " is at " + address;
    }
}
