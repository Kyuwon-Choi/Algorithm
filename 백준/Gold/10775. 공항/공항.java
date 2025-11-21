

import java.util.*;
import java.io.*;


public class Main {

    static int g;
    static int p;
    static int[] gate;
   
   
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //StringTokenizer st;
        
       
         g = Integer.parseInt(br.readLine());
         p = Integer.parseInt(br.readLine());
         gate = new int[g+1];
         int answer=0;
         
		 
		 //st = new StringTokenizer(br.readLine());
         // = Integer.parseInt(st.nextToken());

		 for(int i=1; i<=g; i++) {
			 gate[i]=i;
		 }
		 for(int i=0; i<p; i++) {
			 int tmp = Integer.parseInt(br.readLine());
			 int canUseGate = find(tmp);
			 
			 
			 if(canUseGate!=0) {
				 answer++;
				 union(canUseGate, canUseGate-1);
			 }
			 else break;
		 }
		 
		
    
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        bw.write(String.valueOf(answer));
        bw.flush();
    }
    private static int find(int x) {
    	if(x==gate[x]) {
    		return x;
    	}
    	return gate[x]=find(gate[x]);
    	}
    
    private static void union(int x, int y) {
    	x=find(x);
    	y=find(y);
    	
    	if (x!=y) gate[x]=y;
    	
    

    		
    }
    


    
    
    
}