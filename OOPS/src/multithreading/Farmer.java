package multithreading;

public class Farmer extends Thread {
    Market market;
    String fruit;
    int count, tries;

    Farmer(Market market, String fruit, int count, int tries) {
        this.market = market;
        this.fruit = fruit;
        this.count = count;
        this.tries = tries;
        this.start();
    }

    @Override
    public void run() {
        for (int i = 0; i < count; i++) {
            market.addFruit(fruit, tries);
            try {
                sleep(452);
            } catch (InterruptedException e) {
                System.out.println("Caught InterruptedException");
            }
        }
    }
}
