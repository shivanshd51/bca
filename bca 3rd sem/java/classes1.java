class Student {
    String name;
    int age;

    public void info(){
        System.out.print("name of Student:");
        System.out.println(this.name);
        System.out.print("age of Student:");
        System.out.println(this.age);
    }
}
public class classes1 {
    public static void main(String[] args) {
        Student stu1 = new Student();
        stu1.name="Shivansh";
        stu1.age=21;

        stu1.info();
    }

}
