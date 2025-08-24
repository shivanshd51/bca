public class project2 {
    public static void main(String[] args) {
        // pen=10 copy=40

        int wallet = 50;

        if(wallet<10){
            System.out.println("can't buy anything");
        }
        else if(wallet==10){
            System.out.println("can buy pen");
        }
        else if(wallet==40){
            System.out.println("can buy copy");
        }
        else if(wallet==50){
            System.out.println("can buy both");
        }
    }
}
