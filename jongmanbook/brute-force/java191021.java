package com.milkyway.jongman;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class java191021 {

	public static void main(String[] args) throws Exception {
		// 안정적인 쌍 만들기
		// 모든 참가자가 10명씩이라고 가정
		int n = 10;
		int[][] wpriority = input(n);
		int[][] mpriority = input(n);
		int[] answer = matching(n, wpriority, mpriority);
		print(answer);
		
	}
	
	public static int[][] input(int n) throws Exception {
		int[][] priority = new int[n][n];
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int idx=0 ; idx < n ; idx++ ) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int jdx=0 ; jdx<n ; jdx++ ) {
				priority[idx][jdx] = Integer.parseInt(st.nextToken());
			}
		}
		return priority;
	}
	
	public static int[] matching(int n, int[][] wpriority, int[][] mpriority) {
		// 남자 기준으로 배열 생성
		int[] curmatching = new int[n];
		// 여자가 짝을 찾았는지에 대해 check하는 배열
		boolean[] check = new boolean[n];
		// 여자가 다음 선호하는 남자를 기억하기 위한 배열
		int[] nextman = new int[n];
		for (int idx=0 ; idx<n ; idx++) {
			// 아직 남자에게 짝이 없다는 뜻의 -1로 초기화
			curmatching[idx] = -1;
		}
		boolean allmatched = false;
		// 모두 매칭될 때까지
		while (!allmatched) {
			allmatched = true;
			// 모든 여자를 돌면서
			for (int idx=0 ; idx<n ; idx++) {
				// 여자에게 이미 짝이 있다면 continue;
				if (check[idx]) continue;
				// 여자가 다음으로 선호하는 남자
				int he = wpriority[idx][nextman[idx]];
				nextman[idx]++;
				// 아직 남자에게 짝이 없다면
				if (curmatching[he] == -1) {
					curmatching[he] = idx;
					check[idx] = true;
				}
				else{
					// 남자에게 짝이 이미 있다면 그 남자를 뺐거나, 차지하지 못하거나 이므로
					// allmatched는 항상 false가 된다.
					allmatched = false;
					if (mpriority[he][curmatching[he]] < idx) {
						check[curmatching[he]] = false;
						curmatching[he] = idx;
						check[idx] = true;
					}
				}
			}
		}
		
		return curmatching;
	}
	
	public static void print(int[] answer) {
		for (int idx=0 ; idx<answer.length ; idx++) {
			System.out.printf("%dth man mathched with %dth woman\n", idx, answer[idx]);
		}
	}

}
