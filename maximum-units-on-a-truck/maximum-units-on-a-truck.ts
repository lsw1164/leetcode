function maximumUnits(boxTypes: number[][], truckSize: number): number {
    return boxTypes.sort((a,b) => b[1] - a[1])
        .reduce((acc, boxType) => {
        const [boxCnt, unitPerBox] = boxType;
        const nextAcc = acc+Math.min(truckSize, boxCnt)*unitPerBox;
        truckSize = Math.max(0, truckSize-boxCnt);
        return nextAcc;
    }, 0)
};