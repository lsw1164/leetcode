function leastInterval(tasks: string[], n: number): number {
    
    if(n === 0) {
        return tasks.length;
    }
    
    const cntTable = Array(26).fill(0);
    
    tasks.forEach(task => {
        const alphabetCode = task.charCodeAt(0) - 65;
        cntTable[alphabetCode]++;
    });
    
    cntTable.sort((a,b) => a-b);
    
    const maxCnt = cntTable.pop();
    let idleTime = (maxCnt - 1) * n
    
    while(cntTable.length > 0 && idleTime > 0) {
        idleTime -= Math.min(maxCnt - 1, cntTable.pop());
    }
    
    idleTime = Math.max(0, idleTime);
    
    return idleTime + tasks.length;
};