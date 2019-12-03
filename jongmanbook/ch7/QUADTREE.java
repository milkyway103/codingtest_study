package com.milkyway.jongman;

public class QUADTREE {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	static char[][] decompressd = new char[Integer.MAX_VALUE][Integer.MAX_VALUE];
	
	public static void decompress(String s, int pos, int y, int x, int size) {
		// 한 글자를 검사할 때마다 포인터 역할을 하는 변수를 한 칸 앞으로 옮긴다.
		char cur = s.charAt(pos);
		pos++;
		// 기저 사례 : 첫 글자가 b 또는 w인 경우
		if(cur == 'b' || cur == 'w') {
			for (int dy = 0 ; dy < size ; ++dy) {
				for (int dx = 0 ; dx < size ; ++dx) {
					decompressd[y+dy][x+dx] = cur;
				}
			}
		}
		else {
			// 네 부분을 각각 순서대로 압축 해제한다.
			int half = size/2;
			decompress(s, pos, y, x, half);
			decompress(s, pos, y, x+half, half);
			decompress(s, pos, y+half, x, half);
			decompress(s, pos, y+half, x+half, half);
		}
		
	}
	
	static int pos;
	
	public static String reverse(String s) {
		char cur = s.charAt(pos);
		pos++;
		if (cur == 'b' || cur == 'w') return cur + "";
		String upperLeft = reverse(s);
		String upperRight = reverse(s);
		String lowerLeft = reverse(s);
		String lowerRight = reverse(s);
		// 위와 아래 조각들 위치를 바꾼다.
		return "x" + lowerLeft + lowerRight + upperLeft + upperRight;
	}

}
