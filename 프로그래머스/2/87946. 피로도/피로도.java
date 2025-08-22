import java.util.*;
class Solution {
    int answer=0;
    public int solution(int k, int[][] dungeons) {
        boolean[] visit = new boolean[dungeons.length];
        int cnt=0;
        dfs(cnt,k, dungeons, visit);
        return answer;
    }
    
    void dfs(int cnt, int hp, int[][] dungeons, boolean[] visit){
            if(answer<cnt) answer=cnt;
        
            for(int i = 0; i<dungeons.length; i++){
                if(!visit[i] && hp>=dungeons[i][0]){
                    visit[i]=true;
                    dfs(cnt+1, hp-dungeons[i][1], dungeons, visit);
                    visit[i]=false;
                }
            }
        
        }
}