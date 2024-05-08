package BaekJava.BronzeV;

import java.util.Scanner;

public class 윤년 {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int year=s.nextInt();
        if(year%400==0){
            System.out.print(1);
        }
        else if(year%4==0&&year%100!=0){
            System.out.print(1);
        }
        else{
            System.out.print(0);
        }
    }
}
