import java.util.*;
import java.io.*;


public class Main {

    static int n, p, k;
    //p: 케이블선 개수, k: 공짜 케이블선 개수
    static int[][] graph;


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        p = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        graph = new int[n][n];
       
        for(int i=0; i<n;i++) {
        	for(int j=0; j<n; j++) {
        		
        		graph[i][j]=0;
   
        	}
        }
        
        for(int i=0; i<p;i++) {
        	st = new StringTokenizer(br.readLine());
        	int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            
            graph[u-1][v-1]=w;
            graph[v-1][u-1]=w;
         
        }
        
        
        int left=0;
        int right=1000001;
        int answer=-1;
        
        while(left<=right) {
        	int mid = (left+right)/2;
        	
        	if (dijkstra(mid)){
        		
        		answer=mid;
        		right=mid-1;
        		
        	}
        	else {
        		left=mid+1;
        	}
        }
        
   

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));



        bw.write(String.valueOf(answer));
        bw.flush();
    }
    private static boolean dijkstra(int x) {
    	
    	int[] dist = new int[n];
    	
    	Arrays.fill(dist, Integer.MAX_VALUE);
    	
    	
    	PriorityQueue<int []> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
    	
    	dist[0]=0;
    	
    	pq.add(new int[] {0,0});
    	
    	while(!pq.isEmpty()) {
    		
    		int[] curr = pq.poll();
    		int u = curr[0];
    		int used = curr[1];
    		
    		if(used > dist[u]) continue;
    		
    		for(int i=0; i<n; i++) {
    			int weight = graph[u][i];
    			
    			if(weight != 0) {
    				int free=0;
    				if(weight>x) {
    					free=1;
    				}
    				int totalFree = used+free;
    				if(totalFree < dist[i]) {
    					dist[i] = totalFree;
    					pq.add(new int[] {i, totalFree});
    				}
    			}
    		}
    	}
    	
    	
    	
    	return dist[n-1]<=k;
    	
    	
 
    }
}