class LRUCache {
  //数组实现lru缓存
  constructor(capacity) {
    this.capacity = capacity
    this.cacheArray = []
  }

  getCache(cache) {
    for (let i = 0; i < this.cacheArray.length; i++) {
      if (cache === this.cacheArray[i]) {
        return i
      }
      return -1
    }
  }
  putCache(cache) {
    let idx = this.getCache(cache)
    if (this.cacheArray.length < this.capacity) {
      if (idx !== -1) {
        this.cacheArray.splice(idx, 1)
        this.cacheArray.unshift(cache)
      } else {
        this.cacheArray.unshift(cache)
      }
    } else {
      if (idx !== -1) {
        this.cacheArray.splice(idx, 1)
        this.cacheArray.unshift(cache)
      } else {
        this.cacheArray.pop()
        this.cacheArray.unshift(cache)
      }
    }
  }
}
