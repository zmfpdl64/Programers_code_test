#include<stdio.h>

int main(void) {
    int h = 5;
    draw1(h);


}

void draw1(int h) {
    if(h == 0) {
        return ;
    }
    draw1(h -1 );
    for(int i = 0; i < h; i++) {
        printf("*");
    }
    printf("\n");
}

void draw2(int h) {
    for(int o = 0; o < h; o++) {
        for()
    }
    
}