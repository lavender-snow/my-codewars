package kata

import "math"

func s(n int) int{
  res := 1
  for i := 2; i<=int(math.Pow(float64(n),0.5)); i++{
    if n%i == 0{
      res += i
      div := n/i
      if i != div{
        res += div
      }
    }
  }
  return res
}

func Buddy(start, limit int) []int {
  calc := make(map[int]int)
  for i := start; i <= limit; i++{
    n := s(i)
    if n <= start{
      continue
    }
    calc[i] = n
    var m int
    if _,exist := calc[n-1]; exist{
      m = calc[n-1]
    }else{
      m = s(n-1)
      calc[n-1] = m
    }
    if m-1 == i{
      return []int{m-1,n-1}
    }
  }
  return nil
}