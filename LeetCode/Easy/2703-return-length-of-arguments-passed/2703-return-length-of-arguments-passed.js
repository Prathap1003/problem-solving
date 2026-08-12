/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    let sum = 0
    for(i in args){
        sum+=1
    }
    return sum
};

/**
 * argumentsLength(1, 2, 3); // 3
 */