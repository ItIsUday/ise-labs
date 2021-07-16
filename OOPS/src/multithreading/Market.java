package multithreading;

import java.util.ArrayList;

public class Market {
    private final int fruitsNumber;
    private final ArrayList<String> fruits;


    Market(int fruitsNumber) {
        if (fruitsNumber <= 0) {
            throw new IllegalArgumentException("Number of fruits has to be positive");
        }
        this.fruitsNumber = fruitsNumber;
        this.fruits = new ArrayList<>();
    }

    synchronized boolean isFull() {
        return fruits.size() == this.fruitsNumber;
    }

    synchronized boolean isEmpty() {
        return fruits.isEmpty();
    }

    synchronized void addFruit(String fruit, int tries) {
        int i = 0;
        while (isFull()) {
            if (i == tries) {
                System.out.println("Farmer gave up adding " + fruit + " after " + tries + " failed attempts\n");
                return;
            }
            System.out.println("Farmer trying to add " + fruit);
            System.out.println("Market is full\n");
            try {
                wait(1000);
            } catch (InterruptedException e) {
                System.out.println("Caught InterruptedException");
            }
            i++;
        }

        fruits.add(fruit);
        System.out.println("Farmer added " + fruit);
        displayFruits();
        System.out.println();
        notify();
    }

    synchronized void buyFruit(String fruit, int tries) {
        int i = 0;
        while (isEmpty() || !fruits.contains(fruit)) {
            if (i == tries) {
                System.out.println("Consumer gave up buying " + fruit + " after " + tries + " failed attempts\n");
                return;
            }
            System.out.println("Consumer trying to buy " + fruit);
            System.out.println(fruit + " is out of stock\n");
            try {
                wait(1000);
            } catch (InterruptedException e) {
                System.out.println("Caught InterruptedException");
            }
            i++;
        }

        fruits.remove(fruit);
        System.out.println("Consumer bought " + fruit);
        displayFruits();
        System.out.println();
        notify();
    }

    synchronized public void displayFruits() {
        System.out.println("fruits = " + fruits);
    }
}