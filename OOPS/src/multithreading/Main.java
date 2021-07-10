package multithreading;

public class Main {
    public static void main(String[] args) {
        Market market = new Market(15);

        new Farmer(market, "Apple", 7, 5);
        new Farmer(market, "Grapes", 6, 7);
        new Farmer(market, "Watermelon", 5, 3);
        new Farmer(market, "Orange", 8, 2);

        new Consumer(market, "Grapes", 7, 4);
        new Consumer(market, "Apple", 6, 3);
        new Consumer(market, "Orange", 2, 5);
        new Consumer(market, "Watermelon", 4, 2);
    }

}
