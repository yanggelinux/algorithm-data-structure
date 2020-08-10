class Stack {
  //js 数组实现栈
  constructor(cap) {
    this.cap = cap
    this.stack = []
  }
  push(item) {
    if (!this.isFull()) {
      this.stack.push(item)
    } else {
      console.log("stack is full")
    }
  }
  pop() {
    if (!this.isEmpty()) {
      return this.stack.pop()
    } else {
      console.log("stack is empty")
    }
  }
  isEmpty() {
    return this.stack.length === 0
  }
  isFull() {
    return this.stack.length === this.cap
  }
  length() {
    return this.stack.length
  }
  clear() {
    this.stack = []
  }
  travel() {
    console.log(this.stack)
  }
}

class Browser {
  //用栈实现浏览器的前进和后退功能
  constructor() {
    this.stackA = new Stack(10)
    this.stackB = new Stack(10)
    this.curPage = null
  }
  clickLink(page) {
    //点击链接，跳转到新页面，这时候stack A里面存放页面
    this.curPage = page
    this.stackA.push(page)
    //清空stack B
    this.stackB.clear()
  }
  clickForward() {
    //点击前进按钮,从stack B 取页面
    if (!this.stackB.isEmpty()) {
      let page = this.stackB.pop()
      this.curPage = page
      this.stackA.push(page)
    } else {
      console.log("不能前进")
    }
  }
  clickBackward() {
    //点击后退按钮 从stack A 里面取数据
    if (!this.stackA.isEmpty()) {
      let page = this.stackA.pop()
      this.curPage = page
      this.stackB.push(page)
    } else {
      console.log("不能后退")
    }
  }
  print() {
    console.log("当前页面:", this.curPage)
    console.log("stackA is:", this.stackA)
    console.log("stackB is:", this.stackB)
  }
}

// stack = new Stack(5)
// stack.push(1)
// stack.push(2)
// stack.push(3)
// stack.push(4)
// stack.push(5)
// stack.push(6)
// stack.travel()
// console.log(stack.pop())
// stack.travel()
borwser = new Browser()
borwser.clickLink("PageA")
borwser.clickLink("PageB")
borwser.clickLink("PageC")
borwser.clickLink("PageD")
borwser.print()
borwser.clickForward()
borwser.print()
borwser.clickBackward()
borwser.print()
borwser.clickBackward()
borwser.print()
