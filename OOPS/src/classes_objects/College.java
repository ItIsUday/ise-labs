package classes_objects;

class College {

    String name;
    Address address;

    College(String name, Address address) {
        this.name = name;
        this.address = address;
    }

    @Override
    public String toString() {
        return "College " + name + " is at " + address;
    }
}
