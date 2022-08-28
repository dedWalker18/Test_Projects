import java.util.*;
class Customer{
  String name;
  ArrayList<String> items;
  public Customer(String n, ArrayList<String> itm){
    this.name = n;
    this.items = itm;
  }
  public Customer(Customer c){
  // copy the values as shown in the test cases to create new object
  c.name = this.name;
  }
  public String toString(){
  // Override the toString() method
    return c.name;
  }
}
public class Test{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    ArrayList<String> p1 = new ArrayList<String>();
    String n = sc.next();
    p1.add(sc.next());
    p1.add(sc.next());
    Customer c1 = new Customer(n,p1);
    Customer c2 = new Customer(c1);
    c2.name = sc.next();
    c2.items.add(sc.next());
    System.out.println(c1 + "\n" + c2);
  }
}    