package teset1;

import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;

public class teset1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int [] dx = {-1, 1, 0, 0};
		int [] dy = {0, 0, -1, 1};
		
		int T = sc.nextInt();
		
		for (int tc = 0; tc < T; tc++) {
			int n = sc.nextInt();
			int m = sc.nextInt();
			
			int [][] arr = new int[n][m];
					
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					arr[i][j] = sc.nextInt();
					
				}
				
			}
			
//			/========================입력 완료
			
			int max_num = 0;
			int num = 0;
			int nx;
			int ny;
			
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					num = arr[i][j];
					
					for (int d = 0; d < 4; d++) {
						nx = i + dx[d]; 
						ny = j + dy[d];
						
						if (0 <= nx && n > nx && 0 <= ny && m > ny) {
							num += arr[nx][ny] ;
						}
						
					}
					
					if (num > max_num) {
						max_num = num;
					}
					
				}
				
			}
			
			
			System.out.println("#" +(tc+1)+ " " + max_num);
			
			
		}
		
	}
}
