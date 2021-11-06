/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    
    const domainMap = new Map();
    
    cpdomains.forEach(cpdomain => {
        const [visitCnt, domain] = cpdomain.split(' ');
        getToalSubDomains(domain).forEach(subDomain => {
            const prev = domainMap.get(subDomain) ?? 0;
            domainMap.set(subDomain, prev + +visitCnt);
        });
    });
    
    return [...domainMap].map(entry => `${entry[1]} ${entry[0]}`);
};
    

function getToalSubDomains(domain) {
    const subDomains = [];
    let startIdx = 0;

    do {
        const subDomain = domain.slice(startIdx)
        startIdx = domain.indexOf('.', startIdx) + 1;
        subDomains.push(subDomain);
    } while(startIdx > 0);

    return subDomains;
}