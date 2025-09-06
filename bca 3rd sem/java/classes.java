class Pen{
    String color;
    String type;

    public void write(){
        System.out.println(this.color);
        System.out.println(this.type);
    }
}

public class classes {

    public static void main(String[] args) {
        Pen pen1 = new Pen();
        pen1.color="blue";
        pen1.type="gel";
        // System.out.println(pen1.color);
        // System.out.println(pen1.type);

        Pen pen2 = new Pen();
        pen2.color ="black";
        pen2.type ="ball";
        // System.out.println(pen2.color);
        // System.out.println(pen2.type);

        pen1.write();

    }
}