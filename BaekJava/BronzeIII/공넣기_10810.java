package BaekJava.BronzeIII;
import java.io.*;
import java.util.*;
public class 공넣기_10810 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<Integer> basket = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            basket.add(0);
        }
        for (int t = 0; t < m; t++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken()) - 1;
            int j = Integer.parseInt(st.nextToken()) - 1;
            int k = Integer.parseInt(st.nextToken());

            for (; i < j + 1; i++) {
                basket.set(i, k);
            }
        }
        for (int i = 0; i < n; i++) {
            bw.write(String.valueOf(basket.get(i))+" ");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
