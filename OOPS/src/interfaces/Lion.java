package interfaces;

public class Lion implements TiredAnimal {
    public Lion() {
        eat();
        sound();
        boast();
        home();
        sleep();
    }

    @Override
    public void eat() {
        System.out.println("I usually eat hoofed animals");
    }

    @Override
    public void sound() {
        System.out.println("I roar");
    }

    @Override
    public void sleep() {
        System.out.println("I sleep around 20 hours a day");
    }

    @Override
    public void home() {
        System.out.println("I live in my den");
    }

    public void boast() {
        System.out.println("I am the king of the jungle");
    }
}
