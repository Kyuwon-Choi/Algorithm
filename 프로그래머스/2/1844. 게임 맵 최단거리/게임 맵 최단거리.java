import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int rows = maps.length;
        int cols = maps[0].length;

        boolean[][] visited = new boolean[rows][cols];

        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{0, 0, 1});
        visited[0][0] = true; 

        int[] dx = {0, 1, -1, 0};
        int[] dy = {1, 0, 0, -1};

        while (!q.isEmpty()) { 
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            int dist = current[2]; 

            if (x == rows - 1 && y == cols - 1) {
                return dist;
            }

            for (int i = 0; i < 4; i++) {
                int cx = x + dx[i];
                int cy = y + dy[i];

                if (cx >= 0 && cx < rows && cy >= 0 && cy < cols) {
                    if (!visited[cx][cy] && maps[cx][cy] == 1) {
                        visited[cx][cy] = true; 
                        q.add(new int[]{cx, cy, dist + 1}); 
                    }
                }
            }
        }

        return -1;
    }
}