function reverse(x: number): number {
    const MAX_INT = ~(1<<31);
    const MIN_INT = 1<<31;
    
    const reversed = x >= 0 ? 
          Number(`${x}`.split('').reverse().join("")) : 
         -Number(`${x}`.slice(1).split('').reverse().join(""));
    
    return MIN_INT <= reversed && reversed <= MAX_INT ? reversed : 0;
};