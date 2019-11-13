package com.milkyway.boj;

import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

public class boj_13460 {
	
	static int[] dx = {1, 0, -1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int n;
	
	static char[][] arr;
	static boolean[][][][] check;
	static Queue<int[]> queue = new LinkedList<int[]>();

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		arr = new char[n][m];
		check = new boolean[n][m][n][m];
		
		for (int idx=0 ; idx<n ; idx++) {
			String s = br.readLine();
			for(int jdx=0 ; jdx<m ; jdx++) {
				arr[idx][jdx] = s.charAt(jdx);
			}
		}
		
		int rx=0, ry=0, bx=0, by=0, depth=1;
		
		for (int idx=0 ; idx<n ; idx++) {
			for (int jdx=0 ; jdx<m ; jdx++) {
				if (arr[idx][jdx] == 'R') {
					rx = idx;
					ry = jdx;
				}
				else if (arr[idx][jdx] == 'B') {
					bx = idx;
					by = jdx;
				}
			}
		}
		
		int[] e = {rx, ry, bx, by, depth};
		check[rx][ry][bx][by] = true;
		queue.add(e);
		dfs();

	}
	
	public static void dfs() {
		while(!queue.isEmpty()){
			int[] a = queue.poll();
			if (a[4] > 10) break;
			for(int idx=0 ; idx<4 ; idx++) {
				int[] nr = new int[3];
				int[] nb = new int[3];
				nr = move(a[0], a[1], dx[idx], dy[idx]);
				nb = move(a[2], a[3], dx[idx], dy[idx]);
				
				if (arr[nb[0]][nb[1]] == 'O') continue;
				if (arr[nr[0]][nr[1]] == 'O') {
					System.out.println(a[4]);
					return;
				}
				
				if (nr[0] == nb[0] && nr[1] == nb[1]) {
					if(nr[2] > nb[2]) {
						nr[0] -= dx[idx];
						nr[1] -= dy[idx];
					}
					else {
						nb[0] -= dx[idx];
						nb[1] -= dy[idx];
					}
				}
				
				if (!check[nr[0]][nr[1]][nb[0]][nb[1]]) {
					check[nr[0]][nr[1]][nb[0]][nb[1]] = true;
					int[] tmp = {nr[0], nr[1], nb[0], nb[1], a[4]+1};
					queue.add(tmp);
				}
				
			}
		}
		
		System.out.println(-1);
		
	}
	
	public static int[] move(int x, int y, int dx_, int dy_) {
		int[] result = new int[3];
		int count = 0;
		while(arr[x+dx_][y+dy_] != '#' && arr[x][y] != 'O') {
			x += dx_;
			y += dy_;
			count++;
		}
		
		result[0] = x;
		result[1] = y;
		result[2] = count;
		
		return result;
	}

}
