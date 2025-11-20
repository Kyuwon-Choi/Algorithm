import java.util.*;
import java.io.*;


public class Main {

    static int n;
    static int k;
    static int[] snow;
    static int min=1000000000;
   
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
       
         n = Integer.parseInt(br.readLine());
         snow = new int[n];
         
		 
		 st = new StringTokenizer(br.readLine());
		 
		 for(int i=0; i<n; i++) {
			 snow[i] = Integer.parseInt(st.nextToken());
			 
		 }
		 
		 Arrays.sort(snow);
		 
		for(int i=0; i<n; i++) {
			for(int j=i+1; j<n; j++) {
				find(i, j);
			
			}
			
		}
		
		
		 
		 
		 
		
    
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        bw.write(String.valueOf(min));
        bw.flush();
    }
    
    private static void find(int x, int y) {
    	
    	int start=0;
    	int end=n-1;
    	while(start<end) {
    		if(start==x||start==y) {
    			start++;
    			continue;
    		}
    		if(end==x||end==y) {
    			end--;
    			continue;
    		}
    		min = Math.min(Math.abs((snow[x]+snow[y])-(snow[start]+snow[end])), min);
        	
    		if(snow[start] + snow[end]<snow[x] + snow[y]) {
    			start++;
    		}
    		else {
    			end--;
    		}
    		
    	}
    	
    	
    }
    
    
    
}