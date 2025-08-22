import java.util.*;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for(int i=0; i<commands.length; i++){
            int[] slice = Arrays.copyOfRange(array, commands[i][0]-1,commands[i][1]);
            Arrays.sort(slice);
            answer[i]=(slice[commands[i][2]-1]);
            
        }
        return answer;
    }
}

// import java.util.*;
// class Solution {
//     public int[] solution(int[] array, int[][] commands) {
//         List<Integer> answerList = new ArrayList<>();
        
//         for(int[] command:commands){
//             int[] slice = Arrays.copyOfRange(array, command[0]-1,command[1]);
//             Arrays.sort(slice);
//             answerList.add(slice[command[2]-1]);
            
//         }
//         int[] answer = new int[answerList.size()];
//         for(int i : answerList){
//             answer[i]=answerList.get(i);
//         }
//         return answer;
//     }
// }