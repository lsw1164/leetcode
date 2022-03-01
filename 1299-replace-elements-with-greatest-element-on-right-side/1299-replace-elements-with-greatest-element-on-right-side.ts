function replaceElements(arr: number[]): number[] {
    
    let maxVal = -1;
    const maxOnRight = arr.reverse()
        .map(val => maxVal = Math.max(maxVal, val))
        .reverse()
    
    return arr.map((val, i) => i < arr.length - 1 ? maxOnRight[i + 1] : -1)
};