import java.util.Scanner;

public class project3 {
    public static void main(String[] args) {
        int num = 0;
        do{
            Scanner sc = new Scanner(System.in);
            System.out.println("enter your number:");
            num = sc.nextInt();
            System.out.println("Your number is:");
            System.out.println(num);
        }while(num>=0);
        System.out.println("THE END");
    }
    
}
