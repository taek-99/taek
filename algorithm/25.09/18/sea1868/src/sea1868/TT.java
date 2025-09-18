package sea1868;

import java.io.File;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Iterator;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class TT {
	
	static int n;
	static int [] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
	static int [] dy = {0, 0, 1, -1, 1, -1, 1, -1};
	static boolean [][] visited;
	static int [][] bomb;
	static char [][] board;
	static int nx, ny;
	
	
	public static void bfs(int x, int y) {
		Deque<int[]> q = new ArrayDeque<>();
		
		q.add(new int [] {x, y});
		visited[x][y] = true;
		
		while (!q.isEmpty()) {
			int [] pos = q.pollFirst();
			
			for (int d = 0; d < 8; d++) {
				nx = pos[0] + dx[d];
				ny = pos[1] + dy[d];
				
				if (!(0 <= nx && nx < n && 0 <= ny && ny < n)) continue;
				
				if (visited[nx][ny]) continue;
				
				
				if (bomb[nx][ny] >= 0) visited[nx][ny] = true;
				
				
				if (bomb[nx][ny] == 0) {
					q.add(new int [] {nx, ny});
				}
				
			}
			
		}
		
	}
	
	
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File ("input (4).txt");
		Scanner sc = new Scanner(file);
		
		int T = sc.nextInt();
		for (int tc = 1; tc < T+1; tc++) {
			
			
			n = sc.nextInt();
			visited = new boolean[n][n];
			bomb = new int[n][n];
			board = new char[n][n];
			nx = 0;
			ny = 0;
					
			for (int i = 0; i < n; i++) {
				String row = sc.next();
				board[i] = row.toCharArray();
			}
	
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					visited[i][j] = false;
					
					if (board[i][j] == '*') {
						bomb[i][j] = -999;
						visited[i][j] = true;
						
						for (int d = 0; d < 8; d++) {
							nx = i + dx[d];
							ny = j + dy[d];
							
							if (0 <= nx && nx < n && 0 <= ny && ny < n) {
								bomb[nx][ny] += 1;
								
							}
						}
						
						
					}
				}
			}
		
			int cnt = 0;
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (bomb[i][j] == 0 && !visited[i][j]) {
						bfs(i, j);
						cnt ++;
					}
					
				}
			}
			
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (!visited[i][j]) {
						cnt ++;
					}
				}
				
			}
	
			System.out.println("#"+tc+" "+cnt);
		}
	}
}
