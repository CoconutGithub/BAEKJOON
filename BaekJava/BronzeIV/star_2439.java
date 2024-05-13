package BaekJava.BronzeIV;
import java.io.*;
import java.util.*;

public class star_2439 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int s = Integer.parseInt(br.readLine());
        int b;
        for(int i=1;i<s+1;i++){
            b = s - i;
            bw.write(" ".repeat(b));
            bw.write("*".repeat(i));
            bw.newLine();
        }
        bw.flush();
        bw.close();
        br.close();
    }
}
