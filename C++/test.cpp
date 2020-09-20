#include <stdio.h>

int main()
{

	unsigned char b = 8;
	while (b)
	{
		printf("%u\n", b << 1);
		b = b << 1;
	}
}