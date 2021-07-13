function reverseWords(s: string): string {
    return s.split(' ')
            .reverse()
            .filter(word=>word.trim() !== "")
            .join(" ");
};