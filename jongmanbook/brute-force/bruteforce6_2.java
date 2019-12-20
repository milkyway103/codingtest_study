package com.milkyway.jongman;

import java.util.ArrayList;

public class bruteforce6_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Integer> picked = new ArrayList<Integer>();
		pick(4, picked, 2);
	}
	
	public static void combination(int n, int r, int[] picked, int index, int target) {
		if (r==0) print(picked, index);
		else if(target == n) return;
		else {
			picked[index] = target;
			combination(n, r-1, picked, index+1, target+1);
			combination(n, r, picked, index, target);
		}
	}
	
	public static void print(int[] arr, int length) {
		for (int idx=0 ; idx<length ; idx++ ) {
			System.out.printf("%d ", arr[idx]);
		}
	}
	
	public static void pick(int n, ArrayList<Integer> picked, int toPick) {
		if (toPick == 0) {
			printPicked(picked);
			return;
		}
		int smallest;
		if (picked.isEmpty()) smallest = 0;
		else smallest = picked.get(picked.size()-1) +1;
		for (int next = smallest; next < n ; ++next) {
			picked.add(next);
			pick(n, picked, toPick-1);
			picked.remove(picked.size()-1);
		}
	}
	public static void printPicked(ArrayList<Integer> picked) {
		for (int idx=0 ; idx<picked.size() ; idx++ ) {
			System.out.printf("%d ", picked.get(idx));
		}
		System.out.println();
	}

}
