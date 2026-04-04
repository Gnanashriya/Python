import java.util.*;
public class javabasics
 {
    public static void bintodec(int binNum)
    {
        int pow =0;
        int decnum=0;
        while (binNum >0 );
        {
          int lastdigit=binNum%10;
          decnum =decnum +(lastdigit*(int)Math.pow(2,pow));
          pow++;
          binNum=binNum/10;
        }
        System.out.println("decimal of"+binNum+"="+decnum);
    }
    public static void main(String []args)
    {
     Scanner sc=new Scanner(System.in);
    bintodec(101);
    }
}
