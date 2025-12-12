package boj1546;

import java.util.Scanner;

public class Main1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		double[] array = new double [n];
		
		
		for(int i=0; i < n; i++) {
			array[i] = sc.nextInt();
		}
		
		double  max_ans = 0;
		for(int i = 0 ; i < n ; i++) {
			if (max_ans < array[i]) {
				max_ans = array[i];
			}
		}
		
		for(int i = 0; i < n; i++) {
			array[i] = array[i]/max_ans * 100;
		}
		
		double ans = 0;
		
		for(int i = 0; i < n; i++) {
			
			ans += array[i];
		}
		
		ans = ans/n;
				
		System.out.println(ans);
		

	}

}
