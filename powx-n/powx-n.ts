function myPow(x: number, n: number): number {
    if (n === 0) {
        return 1;
    }
    if (n === 1 || x === 0) {
        return x;
    }
    if (n < 0) {
        return myPow(1/x, -n);
    }
    if (n % 2 === 0) {
        return myPow(x*x, n*0.5);
    }
    return x * myPow(x, n-1);
};