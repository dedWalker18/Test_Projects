import java.util.*;
class FClass1{
  
  public static void main(String[] args){
    try (Scanner sc = new Scanner(System.in)) {
      String s1 = sc.next();
      evenDisplay(s1);
    }
  }


//Define evenDisplay(String) method here

private static void evenDisplay(String s1) {
    for(int i = 0; i <= s1.length(); i=i+2){
        System.out.print(s1.charAt(i));
    }
}
}