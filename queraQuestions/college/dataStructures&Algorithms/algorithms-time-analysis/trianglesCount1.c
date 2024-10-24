// https://quera.org/college/3016/chapter/8233/lesson/146667/?comments_page=1&comments_filter=ALL&submissions_page=1
#include <stdio.h>
int main() {
    int n;
    scanf("%d",&n);
    int counter=0;
    for (int i=1;i<n;i++){
        for(int j=i;j<n;j++){
            for(int k=j;k<n;k++){
                if(i+j+k==n && i+j>k && i+k>j && j+k>i){
                    counter++;
                }
            }
        }
    }
    printf("%d",counter);
    return 0;
}