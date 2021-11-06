/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    
    const domainMap = new Map();
    
    cpdomains.forEach(cpdomain => {
        const [visitCnt, domain] = cpdomain.split(' ');
        getTotalSubDomains(domain).forEach(subDomain => {
            const prev = domainMap.get(subDomain) ?? 0;
            domainMap.set(subDomain, prev + +visitCnt);
        });
    });
    
    return [...domainMap].map(([subDomain, visitCnt]) => `${visitCnt} ${subDomain}`);
};
    

function getTotalSubDomains(domain) {
    const subDomains = [];
    let startIdx = 0;
    do {
        const subDomain = domain.slice(startIdx)
        subDomains.push(subDomain);
        startIdx = domain.indexOf('.', startIdx) + 1;
    } while(startIdx > 0);

    return subDomains;
}