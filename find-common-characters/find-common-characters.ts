
const a2i = (ch: string): number => ch.charCodeAt(0) - 'a'.charCodeAt(0);
const i2a = (num: number): string => String.fromCharCode(num + 'a'.charCodeAt(0)); 

function createVisitCnt(word: string): number[] {
    const visitCnt: number[] = Array<number>(26).fill(0);
    [...word].forEach( ch => visitCnt[a2i(ch)]++ );
    return visitCnt;
}

function commonChars(words: string[]): string[] {
    if(words.length === 1) {
        return [...words[0]]
    }
    
    let curCnts: number[] = createVisitCnt(words[0]);
    for(let i = 1; i < words.length; i++) {
        const nextCnts = createVisitCnt(words[i]);
        curCnts = nextCnts.map((_, idx) =>  Math.min(nextCnts[idx], curCnts[idx]));
    }
    const ans: string[] = [];
    curCnts.forEach((cnt, idx) => {
        while(cnt--) {
            ans.push(i2a(idx));
        };
    });
    return ans;
};