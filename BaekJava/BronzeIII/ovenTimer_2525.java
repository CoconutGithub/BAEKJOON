package BaekJava.BronzeIII;
import java.util.*;
public class ovenTimer_2525 {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int h=s.nextInt();
        int m=s.nextInt();

        int time=s.nextInt();
        if (m+time>=60){
            h+=(m+time)/60;
            if(h>23){
                h%=24;
            }
            m=(m+time)%60;
        }
        else {
            m+=time;
        }
        System.out.print(h+" "+m);
    }
}
