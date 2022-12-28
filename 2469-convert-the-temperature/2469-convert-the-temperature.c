/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
double* convertTemperature(double celsius, int* returnSize){
    *returnSize=2;
    double *array = (double *)malloc(sizeof(double) * (*returnSize));
    double k,f;

    celsius*=100000;
    k=celsius+(273.15*100000);
    f=celsius*1.8+(32*100000);

    array[0]=k/100000;
    array[1]=f/100000;
    
    return array;
}