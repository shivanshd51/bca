import java.util.Scanner;

public class project1 {
    public static void main(String[] args) {
        // taking out percentage of a student out of 5 subject 100 marks of each subject

        Scanner input = new Scanner(System.in);

        System.out.println("enter the english subject marks:");
        int english = input.nextInt();
        System.out.println("enter the hindu subject marks:");
        int hindi = input.nextInt();
        System.out.println("enter the maths subject marks:");
        int maths = input.nextInt();
        System.out.println("enter the sst subject marks:");
        int sst = input.nextInt();
        System.out.println("enter the science subject marks:");
        int science = input.nextInt();

        int total=(english+hindi+maths+sst+science);
        int mm=5;

        float percentage = total/mm;

        System.out.println("The percentage of the student is:");
        System.out.println(percentage);
    }
}
