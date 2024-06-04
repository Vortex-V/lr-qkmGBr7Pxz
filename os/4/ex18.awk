{
        split($0, arr, " ");
        for (idx in arr) {
                printf("\n%d\t%s", idx, arr[idx]);
        }
        printf("\n");
}
