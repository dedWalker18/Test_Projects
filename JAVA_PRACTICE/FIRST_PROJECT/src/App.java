public class App {
    public static void main(String[] args) throws Exception {                    /* static says that function can be called without creating an object */
        System.out.println("Hello World");
        System.out.println(App.sumof2(10, 20));
        System.out.println(App.sumofall(10));
        System.out.println(App.square(6));
    }

    public static int sumof2(int a, int b) {
        int c = a + b; 
        System.out.println("Helu Again");
        return c;
    }

    private static int sumofall(int x){
        int sum = 0;
        for(int i=1; i <= x; i++) {
            sum = sum + i;
        }
        return sum;
    }
    public static String square(int len) {
        for(int i = 1; i < len + 1; i++){
            for(int j = 1; j <= (len - i - 1) / 2; j++){
                System.out.print(" ");
                }
                String str = "*";		 
                System.out.println( str.repeat(Math.abs(i)) );
        }
        return "Good Luck";

    }

}