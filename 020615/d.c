#include <stdio.h>
#include <stdlib.h>

int main() {
	
	char buffer[20];
	char *p, *q;

	scanf("%s", buffer);
	for (p = buffer, q = buffer + strlen(buffer); p < q; p++, q--) {
		if (*p != *q) {
				
		}
	}
	
	return 0;
}
