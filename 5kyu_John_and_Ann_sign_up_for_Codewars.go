package kata

func JohnAndAnn(n int) ([]int,[]int){
  ann := []int{1}
  john := []int{0}
  for i := 1; i < n; i++{
    john = append(john,i-ann[john[i-1]])
    ann = append(ann,i-john[ann[i-1]])
  }
  return john,ann
}

func Ann(n int) []int {
  _, res:= JohnAndAnn(n)
  return res
}
func John(n int) []int {
  res, _:= JohnAndAnn(n)
  return res
}
func SumJohn(n int) int {
  res := 0
  for _,v := range John(n){
    res += v
  }
  return res
}
func SumAnn(n int) int {
  res := 0
  for _,v := range Ann(n){
    res += v
  }
  return res
}