package com.milkyway.boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1182 {
	
	static int answer = 0;
	static int s;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		s = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n];
		
		st = new StringTokenizer(br.readLine());
		for(int idx = 0 ; idx < n ; idx++) {
			arr[idx] = Integer.parseInt(st.nextToken());
		}
		
		dfs(arr, n);
		System.out.print(answer);

	}
	
	public static void dfs(int[] arr, int n) {
		int temp;
		boolean flag;
		for(int idx=0;idx<1<<n;idx++) {
			temp = 0;
			flag = false;
			for(int jdx=0;jdx<n;jdx++) {
				if((idx & 1<<jdx) != 0) {
					temp+=arr[jdx];
					flag = true;
				}
			}
			if (flag == true && temp == s) answer++;
			
		}
	}

}
