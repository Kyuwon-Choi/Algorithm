

import java.util.*;
import java.io.*;


public class Main {

    static int n;
    static int k;
    static int[][] dp;
   
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
       
      
		 st = new StringTokenizer(br.readLine());
		 n = Integer.parseInt(st.nextToken());
		 k = Integer.parseInt(st.nextToken());
		 dp = new int[k+1][n+1];
		 for(int i=0; i<=k; i++) {
			 dp[i][0]=1;
		 }
		 for(int i=0; i<=n; i++) {
			 dp[0][i]=1;
		 }
		 
		for(int i=1;i<k; i++) {
			for(int j=1; j<=n; j++) {
				dp[i][j]=dp[i][j-1];
				dp[i][j]+=dp[i-1][j];
				dp[i][j]%=1000000000;
			}
		}
    
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        bw.write(String.valueOf(dp[k-1][n]));
        bw.flush();
    }
    
    
    
}