package kata

import (
  "fmt"
  "math"
  "strings"
)

func factorization(n int) [][]int{
  arr := [][]int{}
  temp := n
  for i := 2; i < int(math. Pow(float64(n),0.5)+1); i++{
    if temp%i == 0{
      count := 0
      for temp%i==0{
        count++
        temp /= i
      }
      arr = append(arr,[]int{i,count})
    }
  }
  if temp!=1{
    arr = append(arr,[]int{temp,1})
  }
  
  if len(arr) == 0{
    arr = append(arr,[]int{n,1})
  }
  
  return arr
}

func Decomp(n int) string {
  m := make(map[int]int)
  for i := 2; i <= n; i++{
    for _,nums := range factorization(i){
      m[nums[0]] += nums[1]
    }
  }
  
  res := []string{}
  for i := 2; i <= n; i++{
    if _,exist := m[i]; exist{
      temp := ""
      if m[i] == 1{
        temp = fmt.Sprintf("%d",i)
      }else{
        temp = fmt.Sprintf("%d^%d",i,m[i])
      }
      res = append(res,temp) 
    }
  }
  return strings.Join(res," * ")
}