/* Binary search for strings (with blanks) */
#include <stdio.h>
#include <string.h>
int main(){
	char name[10][30], temp[30],skey[30];
	int i,j,first,last,mid,found=0;
	for(i=0;i<10;i++){
		printf("Enter string %d : ",i+1);
		//gets(name[i]) to read strinmg with blanks
		scanf(" %[^\n]",name[i]);
	}
	//Now sorting
	for(i=0;i<9;i++)
	  for(j=0;j<10-i-1;j++) // Bubble sort
	    if(strcmpi(name[j],name[j+1])>0){
	    	strcpy(temp,name[j]);
	    	strcpy(name[j],name[j+1]);
	    	strcpy(name[j+1],temp);
		}
    printf("Sorted Strings:\n");
	for(i=0;i<10;i++)
	   printf("%s\n",name[i]);
	printf("Enter search key : ");
	scanf(" %[^\n]",skey);
	first=0;last=9;
	while(first<=last && !found){
		mid=(first+last)/2;
		if(strcmp(name[mid],skey)>0) last=mid-1;
		else if (strcmp(name[mid],skey)<0) first=mid+1;
		else found=1;
	}
	if(found) printf("Found at %dth position\n",mid+1);
	else printf("Not found\n");
	   
	return (0);   		
}
