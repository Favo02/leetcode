/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function (a) {

  for (let i = 0; i < a.length - 1; i++) {

    // collision
    if (a[i] > 0 && a[i + 1] < 0) {
    
      // same size: both destroyed
      if (a[i] === -a[i + 1]) {
        a.splice(i, 2)
        i -= 2
        continue
      }

      // one bigger than other: remove smaller
      if (Math.abs(a[i]) > Math.abs(a[i + 1])) {
        a.splice(i + 1, 1)
        i-- // keep scanning from current element
      }
      else {
        a.splice(i, 1)
        // go back to scan from previous element because the current one got removed,
        // so the new current one could be in collision with previous
        i -= 2
      }
    }
  }

  return a
}
