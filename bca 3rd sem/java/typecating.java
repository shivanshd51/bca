public class typecating {
    public static void main(String[] args) {
        // implicit example
        double price = 100.00;
        double finalPrice = price + 18;
        System.out.println(finalPrice);

        // explicit example
        int p = 100;
        int fp = p+(int)18.99;
        System.out.println(fp); //result = 118 (hence .99 data is lost)
    }
}
