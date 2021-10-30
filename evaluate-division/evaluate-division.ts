function calcEquation(equations: string[][], values: number[], queries: string[][]): number[] {
    
    const calcMap = new Map();
    equations.flat().forEach((key: string) => !calcMap.has(key) && calcMap.set(key, new Map()));
    
    equations.forEach((equation: string[], idx: number) => {
        const [numerator, denominator] = equation;
        calcMap.get(numerator).set(denominator, values[idx]);
        calcMap.get(denominator).set(numerator, 1/values[idx]);
    });
    
    for(const [first, firstMap] of calcMap) {
        for(const [second, FstDivSec] of firstMap) {
            const secondMap = calcMap.get(second);
            for(const [third, secDivTrd] of secondMap) {
                const thirdMap = calcMap.get(third);
                const fstDivTrd = FstDivSec*secDivTrd;
                firstMap.set(third, fstDivTrd);
                thirdMap.set(first, 1/fstDivTrd);
            }
        }
    }
    
    return queries.map((query: string[]): number => {
        const [numerator, denominator] = query;
        if(!calcMap.has(numerator)) {
            return -1;
        }
        const numeratorMap = calcMap.get(numerator);
        if(!numeratorMap.has(denominator)) {
            return -1;
        }
        return numeratorMap.get(denominator);
    });
};