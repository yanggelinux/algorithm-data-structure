class SingleNode {
  constructor(val) {
    this.next = null
    this.val = val
  }
}
class LinkedList {
  constructor() {
    this.head = null
  }
  isEmpty() {
    //判断链表是否为空
    return this.head === null
  }
  getLength() {
    //获取链表长度
    let length = 0
    let curNode = this.head
    while (curNode !== null) {
      length += 1
      curNode = curNode.next
    }
    return length
  }
  travel() {
    const res = []
    let curNode = this.head
    while (curNode !== null) {
      res.push(curNode.val)
      curNode = curNode.next
    }
    console.log(res)
  }
  add(val) {
    //链表头部添加节点
    let newNode = new SingleNode(val)
    newNode.next = this.head
    this.head = newNode
  }
  append(val) {
    //链表尾部添加节点
    let newNode = new SingleNode(val)
    if (this.isEmpty()) {
      this.head = newNode
    } else {
      let curNode = this.head
      while (curNode.next !== null) {
        curNode = curNode.next
      }
      curNode.next = newNode
    }
  }
  insert(index, val) {
    let newNode = new SingleNode(val)
    if (index <= 0) {
      this.add(val)
    } else if (index > this.getLength()) {
      this.append(val)
    } else {
      let step = 0
      let curNode = this.head
      while (curNode !== null) {
        step += 1
        if (step === index) {
          newNode.next = curNode.next
          curNode.next = newNode
          break
        }
        curNode = curNode.next
      }
    }
  }
  search(val) {
    let curNode = this.head
    let index = 0
    while (curNode !== null) {
      if (curNode.val === val) {
        return index
      }
      curNode = curNode.next
      index += 1
    }
    return -1
  }
  removeByVal(val) {
    let curNode = this.head
    //定义要删除节点的前驱节点
    let prevNode = null
    while (curNode !== null) {
      if (curNode.val === val) {
        if (prevNode === null) {
          //要删除的节点是头节点
          this.head = curNode.next
        } else {
          prevNode.next = curNode.next
        }
        return
      } else {
        prevNode = curNode
        curNode = curNode.next
      }
    }
  }
  removeByIndex(index) {
    let curNode = this.head
    let step = 0
    //定义要删除节点的前驱节点
    let prevNode = null
    while (curNode !== null) {
      if (step === index) {
        if (prevNode === null) {
          //要删除的节点是头节点
          this.head = curNode.next
        } else {
          prevNode.next = curNode.next
        }
        return
      } else {
        step += 1
        prevNode = curNode
        curNode = curNode.next
      }
    }
  }
}

class LRUCache {
  //单链表实现LRU缓存
  constructor(capacity) {
    this.capacity = capacity
    this.cacheArray = new LinkedList()
  }
  getCache(cache) {
    let index = this.cacheArray.search(cache)
    // console.log(index)
    return index
  }
  putCache(cache) {
    let idx = this.getCache(cache)
    let length = this.cacheArray.getLength()
    if (length < this.capacity) {
      if (idx !== -1) {
        this.cacheArray.removeByIndex(idx)
        this.cacheArray.add(cache)
      } else {
        this.cacheArray.add(cache)
      }
    } else {
      if (idx !== -1) {
        this.cacheArray.removeByIndex(idx)
        this.cacheArray.add(cache)
      } else {
        this.cacheArray.removeByIndex(length - 1)
        this.cacheArray.add(cache)
      }
    }
  }
}

// const linkedList = new LinkedList()
// linkedList.append(1)
// linkedList.append(2)
// linkedList.append(3)
// linkedList.append(4)
// linkedList.append(5)
// linkedList.travel()
// console.log(linkedList.search(3))
// linkedList.add(0)
// linkedList.travel()
// linkedList.insert(2, -1)
// linkedList.travel()
// console.log(linkedList.search(-2))
// linkedList.removeByVal(-1)
// linkedList.travel()
// linkedList.removeByIndex(5)
// linkedList.travel()
// console.log(linkedList.isEmpty())
// console.log(linkedList.getLength())
// newNode = new SingleNode(10)
// newNode2 = new SingleNode(11)
// newNode.next = newNode2
// console.log(newNode.val)
// console.log(newNode.next)
lru = new LRUCache(5)
lru.putCache(1)
lru.putCache(2)
lru.putCache(3)
lru.cacheArray.travel()
// console.log(lru.getCache(2))
lru.putCache(2)
lru.cacheArray.travel()
lru.putCache(4)
lru.cacheArray.travel()
lru.putCache(5)
lru.cacheArray.travel()
lru.putCache(6)
lru.cacheArray.travel()
lru.putCache(2)
lru.cacheArray.travel()
