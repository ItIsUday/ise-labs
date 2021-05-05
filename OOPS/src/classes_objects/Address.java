package classes_objects;

class Address {

    String streetNum, city, state, country;

    Address(String streetNum, String city, String state, String country) {
        this.streetNum = streetNum;
        this.city = city;
        this.state = state;
        this.country = country;
    }

    @Override
    public String toString() {
        return streetNum + " street, " + city + " city, " +
                state + " state, " + country + " country";
    }
}
