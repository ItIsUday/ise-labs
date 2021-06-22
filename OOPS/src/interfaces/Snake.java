package interfaces;

public class Snake implements TiredAnimal {
    public Snake() {
        eat();
        sound();
        speciality();
        home();
        sleep();
    }

    @Override
    public void eat() {
        System.out.println("I eat small warm-blooded animals");
    }

    @Override
    public void sound() {
        System.out.println("I hiss");
    }

    @Override
    public void sleep() {
        System.out.println("I sleep around 2 hours a day");
    }

    @Override
    public void home() {
        System.out.println("I usually live under a rock");
    }

    public void speciality() {
        System.out.println("I have no legs and I crawl on my body");
    }
}
