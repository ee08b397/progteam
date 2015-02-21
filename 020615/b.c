#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, i, a, b;
	char *ans;
	
	scanf("%d", &n);
	ans = malloc(sizeof(char) * n);
	for (i = 0; i < n; i++) {	
		scanf("%d %d", &a, &b);
		if (a < b)
			ans[i] = '<';
		else if (a > b)
			ans[i] = '>';
		else
			ans[i] = '=';
	}	
	for (i = 0; i < n; i++)
		printf("%c\n", ans[i]);		
}
