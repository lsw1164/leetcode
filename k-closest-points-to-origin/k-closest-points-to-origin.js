/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    return points.sort((p1, p2) => (p1[0]*p1[0]+p1[1]*p1[1]) - (p2[0]*p2[0]+p2[1]*p2[1]))
        .slice(0, k);
};