public class break1 {
    public static void main(String[] args) {
        // break and continue

        int i = 1;
        while(true){
            if(i==7){
                i=i+1;
                continue;
            }
            System.out.println(i);
            i=i+1;
            if (i>10){
                break;
            }
        }
    }    
}