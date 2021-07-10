package multithreading;

import java.util.ArrayList;

public class Market {
    private final int fruitsNumber;
    private final ArrayList<String> fruits;


    public Market(int fruitsNumber) {
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

    synchronized void addFruit(String fruit) {
        while (isFull()) {
            System.out.println("Farmer trying to add " + fruit);
            System.out.println("Market is full");
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println("Caught InterruptedException");
            }
        }

        fruits.add(fruit);
        System.out.println("Farmer added " + fruit);
        displayFruits();
        notify();
    }

    synchronized void BuyFruit(String fruit) {
        while (isEmpty() || !fruits.contains(fruit)) {
            System.out.println("Consumer trying to buy " + fruit);
            System.out.println(fruit + " is out of stock");
            try {
                wait();
            } catch (InterruptedException e) {
                System.out.println("Caught InterruptedException");
            }
        }

        fruits.remove(fruit);
        System.out.println("Consumer removed fruit " + fruit);
        displayFruits();
        notify();
    }

    synchronized public void displayFruits() {
        System.out.println("fruits = " + fruits);
    }
}