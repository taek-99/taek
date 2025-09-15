package tree;

import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;
import java.io.File;


public class tree1 {
	
	static class TreeNode { 
		int val;
		TreeNode left, right;
		TreeNode(int v) {
			this.val = v;
		}
	}
	
//	전위
	static void preorder(TreeNode root) {
		if (root != null) {
			System.out.print(root.val + " ");
			preorder(root.left);
			preorder(root.right);
		}
	}
	
	
//	중위
	static void inorder(TreeNode root) {
		if (root != null) {
			inorder(root.left);
			System.out.print(root.val + " ");
			inorder(root.right);
		}
	}
	
//	후위
	static void postorder(TreeNode root) {
		if (root != null) {
			postorder(root.left);
			postorder(root.right);
			System.out.print(root.val + " ");
		}
	}
	
	
	
	public static void main(String[] args) throws FileNotFoundException {
		File file = new File("input (3).txt");
		Scanner sc = new Scanner(file);
		
		int n = sc.nextInt();
		
		ArrayList<Integer>[] tree = new ArrayList[n+1];
		for (int i = 1; i < n+1; i++) {
			tree[i] = new ArrayList<>();
		}
		
		
		while (sc.hasNextInt()) {
			int parent = sc.nextInt();
			int child = sc.nextInt();
			tree[parent].add(child);
			
		}
		
		sc.close();
		
		TreeNode[] nodes = new TreeNode[n+1];
		for (int i = 1; i < n+1; i++) {
			nodes[i] = new TreeNode(i);
		}
		
		
		
		
		for (int i = 1; i < n+1; i++) {
			ArrayList<Integer> kids = tree[i];
			if (kids.size() >= 1) {
				nodes[i].left = nodes[kids.get(0)];
				
			}
			
			if (kids.size() == 2) {
				nodes[i].right = nodes[kids.get(1)];
				
			}
			
		}
		
		
		
		TreeNode root = nodes[1];
		
		preorder(root); System.out.println();
		inorder(root); System.out.println();
		postorder(root); System.out.println();
		
		
		
		
		
	}
}
