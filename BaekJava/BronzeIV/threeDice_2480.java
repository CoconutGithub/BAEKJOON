package BaekJava.BronzeIV;

import java.util.*;
public class threeDice_2480 {
    public static void main(String[] args) {
        Scanner s=new Scanner(System.in);
        int dice1=s.nextInt();
        int dice2=s.nextInt();
        int dice3=s.nextInt();
        if(dice1==dice2&&dice1==dice3){
            System.out.print(10000+dice1*1000);
        }
        else if (dice1==dice2) {
            System.out.print(1000+dice1*100);
        }
        else if (dice2==dice3) {
            System.out.print(1000+dice2*100);
        }
        else if (dice1==dice3) {
            System.out.print(1000+dice1*100);
        }
        else {
            if(dice1>dice2&&dice1>dice3){
                System.out.print(dice1*100);
            }
            else if(dice2>dice1&&dice2>dice3){
                System.out.print(dice2*100);
            }
            else {
                System.out.print(dice3*100);
            }
        }

    }
}
