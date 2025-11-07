

import java.util.*;
import java.io.*;


public class Main {

    static int n;
    static int[][] graph;
    static int[][] dp;
    static int INF = 20000000;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        n = Integer.parseInt(br.readLine());

 
        graph = new int[n][n];
       
        for(int i=0; i<n;i++) {
        	 st = new StringTokenizer(br.readLine());
        	 for(int j =0; j<n; j++) graph[i][j] = Integer.parseInt(st.nextToken());
             
        }
        
        dp = new int[n][1 << n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }
        
       int ans = recur(0, 1);
   

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));



        bw.write(String.valueOf(ans));
        bw.flush();
    }
    
    private static int recur(int now, int bit) {
    	if (bit == (1<<n)-1) {
    		if(graph[now][0] == 0) {
    			return INF;
    		}
    		return graph[now][0];
 
    	}
    	
    	if(dp[now][bit] != -1) {
    		return dp[now][bit];
    	}
    	
    	dp[now][bit]=INF;
    	for(int i =0; i<n; i++) {
    		if((bit & (1<<i))==0 && graph[now][i]!=0 ) {
    			int cost = recur(i, bit|(1<<i))+graph[now][i];
    			
    			dp[now][bit] = Math.min(dp[now][bit], cost);
    		}
    	}
    	return dp[now][bit];
    	
    }
    
}