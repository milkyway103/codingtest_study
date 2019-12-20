package com.milkyway.jongman;

import java.util.Scanner;
import java.util.ArrayList;

public class boggle {
	//8개의 가능한 방향
	static final int[][] d = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}, 
			{1, 0}, {1, -1}, {0, -1}, {-1, -1}};
	static boolean ans = false;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String word = input();
		char[][] map = new char[5][5];
		ArrayList<int[]> candidate = findfirst(map, word.charAt(0));
		if (candidate.isEmpty()) { 
			System.out.println("There is no word.");
			return;
		}
		for (int[] start : candidate) {
			hasWord(start[0], start[1], word, 0, map);
			if (ans) {
				System.out.println("There is this word.");
				return;
			}
		}
		System.out.println("There is no word.");
	}
	
	static String input() {
		Scanner in = new Scanner(System.in);
		return in.next();
	}
	
	static ArrayList<int[]> findfirst(char[][] map, char first) {
		ArrayList<int[]> ret = new ArrayList<int[]>();
		
		for (int idx=0 ; idx<5 ; idx++ ) {
			for (int jdx=0 ; jdx<5 ; jdx++ ) {
				if (map[idx][jdx] == first) {
					int[] temp = {idx, jdx};
					ret.add(temp);
				}
			}
		}
		
		return ret;
	}
	
	static void hasWord(int x, int y, String word, int pos, char[][] map) {
		if (pos == word.length()) {
			ans = true;
			return;
		}
		for (int[] dir : d) {
			int nx = x+dir[0];
			int ny = y+dir[1];
			if (0<=nx && nx<5 && 0<= ny && ny<5 && map[nx][ny]==word.charAt(pos)) {
				hasWord(nx, ny, word, pos+1, map);
			}
		}
	}
	
	static boolean jmhasWord(int x, int y, String word, int[][] map) {
		if(!inRange(x, y)) return false;
		if(map[x][y] != word.charAt(0)) return false;
		if(word.length() == 1) return true;
		for(int[] dir : d) {
			int nx = x+dir[0];
			int ny = y+dir[1];
			if(jmhasWord(nx, ny, word.substring(1), map)) return true;
		}
		return false;
	}
	
	static boolean inRange(int x, int y) {
		if (0<=x && x<5 && 0<= y && y<5) return true;
		else return false;
	}

}
