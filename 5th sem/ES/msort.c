#include<stdio.h>
int main(){
   int a[7]={10,20,40,120,200,230,250};
   int b[10]={5,15,25,45,100,110,210,220,257,300};
   int c[17];
   int ai,bi,ci;ai=bi=ci=0;
   while(ai < 7 && bi < 10){
      if(a[ai] < b[bi]) {
         c[ci] =a[ai];ai++;
      }
      else{
         c[ci] =b[bi];bi++;
      }
      ci++;
   }
   while(ai < 7){
      c[ci]=a[ai];ai++;ci++;
   }
   while(bi < 10){
      c[ci] = b[bi];bi++;ci++;
   }

   for(ci=0;ci<17;ci++){
      printf("%d ",c[ci]);
   }

   return 0;
}