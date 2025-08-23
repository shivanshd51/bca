import java.util.Scanner;

public class takinginput {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("enter your age:");
        // int age = input.nextInt();
        // float age = input.nextFloat();
        // String name = input.next();
        String name = input.nextLine();
        System.out.println(name);
    }
}
