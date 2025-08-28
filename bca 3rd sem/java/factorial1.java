import java.util.Scanner;

public class factorial1 {
    public static void factorial(int a){
        int b = 1;
        for(int i=a;i!=0;i--){
            b=b*i;
        }
        System.out.println("Your Factorial is:");
        System.out.println(b);
    }
    public static void main(String[] args) {
        factorial(4);
    }
}
