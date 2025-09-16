package sea1226java;

import java.io.File;
import java.io.FileNotFoundException;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;


public class main {
	
	static int n;
	static boolean a;
	static boolean complete = false;
	static int nx = 0, ny = 0;
	static int[][] board;
	static int [] dx = {-1, 1, 0, 0};
	static int [] dy = {0, 0, -1, 1};
	static int st_x = 0, st_y = 0;  // 출발, 종료 위치 확보
	static int ed_x = 0, ed_y = 0;
	
	static boolean dfs(int x, int y) {
		
		if (x == ed_x && y == ed_y) {
			complete = true;
		}
		
		if (complete) {
			return true;
		}
	
		for (int i = 0; i < 4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			
			if (board[nx][ny] == 0 || board[nx][ny] == 3) {
				board[nx][ny] = 1;
				dfs(nx, ny);
			}
		}
		
		return complete;
	}
	
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("input (4).txt");
		Scanner sc = new Scanner(file);
			
		
		for (int t = 1; t < 11; t++) {
			n = sc.nextInt();  // 입력받아옴
			sc.nextLine();
			complete = false;
			
			board = new int[16][16];
			for (int i = 0; i < 16; i++) {
				String line = sc.nextLine().trim();
				for (int j = 0; j < 16; j++) {
					board[i][j] = line.charAt(j) - '0';
					if (board[i][j] == 2) {
						st_x = i;
						st_y = j;
					}
					
					if (board[i][j] == 3) {
						ed_x = i;
						ed_y = j;
					}
					
				}
			}
			
			
			if (dfs(st_x, st_y)) {
				System.out.println("#"+ n + " "+1);
			}else {
				System.out.println("#"+ n + " "+0);
			}
			
		}
		
	}
}
