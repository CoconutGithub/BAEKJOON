package BaekJava.BronzeII;
import java.io.*;
import java.util.*;
public class reverseBasket {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);
        int[] basket = new int[n];
        for (int i = 0; i < n; i++) {
            basket[i] = i + 1;
        }
        for (int i = 0; i < m; i++) {
            String[] fe = br.readLine().split(" ");
            int f = Integer.parseInt(fe[0])-1;
            int e = Integer.parseInt(fe[1])-1;
            int t = e - f;
            for (int j = 0; j < t/2+1; j++) {
                int temp = basket[f+j];
                basket[f+j] = basket[e-j];
                basket[e - j] = temp;
            }
        }
        for (int i = 0; i < basket.length;i++ ) {
            bw.write(basket[i]+" ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
