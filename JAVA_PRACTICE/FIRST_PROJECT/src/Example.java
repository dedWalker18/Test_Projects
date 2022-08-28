public class Example
{
      public static void main(String args[]) {
          int [] numbers = new int[]{1, 2, 3, 4, 5};

          for(int BSC : numbers)
          {
                if( BSC == 4 )
                {
                      break;
                }
                System.out.println(BSC);
          }
      }
}