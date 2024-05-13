package BaekJava.BronzeIII;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class maxmin_10818 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        List<String> arr = new ArrayList<String>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i =0;i<n;i++){
            arr.add(st.nextToken());
        }
        int max = Integer.parseInt(arr.get(0));
        int min = Integer.parseInt(arr.get(0));
        for(int i =0;i<n;i++){
            if (Integer.parseInt(arr.get(i))>max){
                max = Integer.parseInt(arr.get(i));
            }
            else if (Integer.parseInt(arr.get(i))<min) {
                min = Integer.parseInt(arr.get(i));
            }
        }
        bw.write(min+" "+max);

        bw.flush();
        bw.close();
        br.close();
    }
}
