func solution(w, h int) int64 {
	var a int64 = int64(w)
	var b int64 = int64(h)
	for true {
		if a < b {
			a, b = b, a
		}
		if b == 0 {
			break
		}
		a = a % b

	}

	var answer int64 = int64(w)*int64(h) - (int64(w) + int64(h) - a)
	return answer

}