/*Making copies of txt*/
#include <stdio.h>
#define COPIES 50000

int main (void)	{
	FILE *index = fopen("index.txt", "w") ;			//Creating an index file
	for(int i = 0; i < COPIES; i++) {
		fprintf(index, "text%i.txt\n", i) ;
	}
	fclose(index) ;
	
	
	FILE *index2 = fopen("index.txt", "r") ;
	char name [14] ;
	void copy_file (FILE *src, FILE *dst) ;		//Funk deck
	
	for(int i = 0; i < COPIES; i++)	{				//Creating copies
		FILE *src = fopen("base.txt", "r") ;
		fscanf(index2, "%s", name) ;
		FILE *dst = fopen(name, "w") ;
		copy_file(src, dst) ;
		fclose(src) ;
		fclose(dst) ; 
	}
	fclose(index2) ;
	return 0 ;
}

void copy_file (FILE *src, FILE *dst)	{			//Copy file function
	char c ;
	while ( (c = getc(src)) != EOF )
		putc(c, dst) ;
}
