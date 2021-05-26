package packages.rvce;

import packages.ise.FourthSem;

public class IseDept extends FourthSem {
    public void welcome() {
        System.out.println("Welcome to 4th sem ISE department of RVCE");
    }

    void defaultMethod() {
        System.out.println("Hello from default method in class IseDept");
    }

    private void privateMethod() {
        System.out.println("Hello from private method in class IseDept");
    }

    void accessPrivateMethod() {
        privateMethod();
    }
}
