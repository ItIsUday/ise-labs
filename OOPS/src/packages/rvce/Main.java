package packages.rvce;

import packages.ise.FourthSem;

public class Main {
    public static void main(String[] args) {
        var obj1 = new FourthSem();
        var obj2 = new IseDept();

        obj1.welcome();
        System.out.println();
        obj2.welcome();
        obj2.defaultMethod();
        obj2.accessPrivateMethod();
    }
}
