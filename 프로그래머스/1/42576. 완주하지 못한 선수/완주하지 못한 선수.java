import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> participantMap = new HashMap<>();
        Map<String, Integer> completionMap = new HashMap<>();
        for(String name:participant){
            participantMap.put(name, participantMap.getOrDefault(name, 0)+1);
            
        }
        for(String name:completion){
            completionMap.put(name, completionMap.getOrDefault(name, 0)+1);
            
        }
        for (String key : participantMap.keySet()){
            if(!completionMap.containsKey(key) || !participantMap.get(key).equals(completionMap.get(key))){
                answer= key;
                
            }
        }
        return answer;
    }
}