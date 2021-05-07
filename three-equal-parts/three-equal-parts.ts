function threeEqualParts(arr: number[]): number[] {
    const totalOneCnt = arr.filter(val => val === 1).length;
    
    if(totalOneCnt === 0) {
        return [0, arr.length-1];
    }
    if(totalOneCnt % 3 !== 0) {
        return [-1, -1];
    }
    
    const eachOneCnt = totalOneCnt / 3;
    const firstDelimiter = [1, eachOneCnt+1, 2*eachOneCnt+1];
    const lastDelimiter = [eachOneCnt, 2*eachOneCnt, 3*eachOneCnt];
    
    const firsts: number[] = [];
    const lasts: number[] = [];
    
    let oneCnt = 0;
    arr.forEach((val: number, pos: number) => {
        if(val === 0) {
            return;
        }
        oneCnt++;
        if(firstDelimiter.includes(oneCnt)) {
            firsts.push(pos);
        }
        if(lastDelimiter.includes(oneCnt)) {
            lasts.push(pos);
        }
    });
    
    const [f1, f2, f3] = firsts;
    const [l1, l2, l3] = lasts;
    const p1 = arr.slice(f1, l1+1).join("");
    const p2 = arr.slice(f2, l2+1).join("");
    const p3 = arr.slice(f3, l3+1).join("");
    
    if(p1 !== p2 || p2 !== p3 || p3 !== p1 ) {
        return [-1, -1];
    }
    
    const x = f2-l1-1, y = f3-l2-1, z = arr.length-l3-1;
    
    if (x < z || y < z) {
        return [-1, -1];
    }
    
    return [l1+z, l2+z+1];
}
