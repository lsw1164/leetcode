/**
 Do not return anything, modify s in-place instead.
 */

function reverseInPlace(s: string[], left: number, right: number) {
    while(left < right) {
        [s[left], s[right]] = [s[right], s[left]];
        left++, right--;
    }
    return s;
}

function indexOfLetter(s: string[], start: number): number {
    for(let i = start; i < s.length; i++) {
        if (s[i] !== ' ') return i;
    }
    return -1;
}

function indexOfSpace(s: string[], start: number): number {
    for(let i = start; i < s.length; i++) {
        if (s[i] === ' ') return i;
    }
    return -1;
}

function reverseWords(s: string[]): void {
    reverseInPlace(s, 0, s.length-1);
    s.push(" ")
    let slow = 0, fast = indexOfLetter(s, 0);
    while(fast >= 0 && fast < s.length) {
        fast = indexOfSpace(s, fast) - 1;
        reverseInPlace(s, slow, fast);
        slow = indexOfSpace(s, fast) + 1
        fast = slow + 1;
    }
    s.pop()
};