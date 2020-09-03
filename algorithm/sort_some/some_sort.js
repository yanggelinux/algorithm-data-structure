//冒泡排序

function bubbSort(nums) {
  const length = nums.length
  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      if (nums[i] > nums[j]) {
        //es6 两数交换
        // ;[nums[i], nums[j]] = [nums[j], nums[i]]
        let tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
      }
    }
  }
}

function bubbSort2(nums) {
  //优化。当某次冒泡操作已经没有数据交换时，说明已经达到完全有序，不用再继续执行后续的冒泡操作。
  const length = nums.length
  for (let i = 0; i < length; i++) {
    //退出标示
    let flag = false
    for (let j = 0; j < length - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        //es6 两数交换
        // ;[nums[i], nums[j]] = [nums[j], nums[i]]
        let tmp = nums[j]
        nums[j] = nums[j + 1]
        nums[j + 1] = tmp
        flag = true
      }
    }
    if (!flag) {
      break
    }
  }
}

// let nums = [2, 1, 4, 3, 8, 5]
// bubbSort2(nums)
// console.log(nums)

//插入排序
function insertSort(nums) {
  length = nums.length
  for (let i = 1; i < length; i++) {
    let value = nums[i] //要插入的值
    let j = i - 1 //插入的位置
    //插入的位置的值nums[j]要小于等于插入的值
    while (j >= 0 && nums[j] > value) {
      nums[j + 1] = nums[j] //移动数据
      j -= 1
    }
    console.log(j, nums)
    nums[j + 1] = value
  }
}
nums = [2, 1, 4, 3, 8, 5, 9, 6]
insertSort(nums)
console.log(nums)

// function selectSort(nums) {
//   //选择排序
//   length = nums.length
//   for (let i = 0; i < length; i++) {
//     let minIdx = i
//     for (let j = i + 1; j < length; j++) {
//       if (nums[j] < nums[minIdx]) {
//         minIdx = j
//       }
//     }
//     let tmp = nums[i]
//     nums[i] = nums[minIdx]
//     nums[minIdx] = tmp
//   }
// }

// nums = [2, 1, 4, 3, 8, 5, 9, 6]
// selectSort(nums)
// console.log(nums)
