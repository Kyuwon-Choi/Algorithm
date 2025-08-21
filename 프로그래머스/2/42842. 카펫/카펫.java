import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int y=3;
        int total = brown+yellow;
        int x=total;
        while(y<=x){
            if(total%y==0){
                x=total/y;
                if((x-2)*(y-2)==yellow)
                {
                    answer[0]=x;
                    answer[1]=y;
                    break;
                }
            }
            y++;
            
        }
        
        return answer;
        
    }
}

