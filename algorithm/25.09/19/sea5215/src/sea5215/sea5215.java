package sea5215;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;

public class sea5215 {
	
	
	public static void dfs(int idx, int price, int cal) {
		if (cal > l) {
			return ;
		}else {
			if (price > max_num) {
				max_num = price;
			}
		}
		
		if (idx==n) {
			return;
		}
		
	
		dfs(idx + 1, price, cal);
		dfs(idx + 1, price + hambuger[idx][0], cal + hambuger[idx][1]);
		
	}
	
	
	
	static int T;
	static int n;
	static int l;
	static int max_num;
	static int [][] hambuger;
	
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("sample_input (17).txt");
		Scanner sc = new Scanner(file);
		
		T = sc.nextInt();
		
		for (int tc = 1; tc < T+1; tc++) {
			
			n = sc.nextInt();
			l = sc.nextInt();
			
			hambuger = new int [n][2];
			 
			for (int i = 0; i < n; i++) {
				hambuger[i][0] = sc.nextInt();
				hambuger[i][1] = sc.nextInt();
			}
			
			
			max_num = 0;
			dfs(0, 0, 0);
			
		
			System.out.println("#" + tc + " " + max_num);
			
		}
		sc.close();
	}
	
}
