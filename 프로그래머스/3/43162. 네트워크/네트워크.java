import java.util.*;

class Solution {
    boolean[] visit;
    int[][] computers;
    int n;
    
    public int solution(int n, int[][] computers) {
        this.n = n;
        this.computers = computers;
        this.visit = new boolean[n];
        
        int cnt=0;
        for(int i=0; i<n; i++){
            if(!visit[i]){
                bfs(i);
                cnt++;
                
            }
        }
        return cnt;
    }
    public void bfs(int com){
            Queue<Integer> q = new LinkedList<>(); 
            q.add(com);
            visit[com]=true;
            while(!q.isEmpty()){
                int e= q.poll();
                for(int i=0; i<n; i++){
                    if(computers[e][i]==1 && !visit[i]){
                        q.add(i);
                        visit[i]=true;
                    }
                }
            }
            
            
        }
}