package main

func isIsomorphic(s string, t string) bool {
	mapping1 := make(map[rune]rune)
	mapping2 := make(map[rune]rune)

	for i := range s {

		f, t := rune(s[i]), rune(t[i])

		if val, ok := mapping1[f]; ok && val != t {
			return false
		}
		if val, ok := mapping2[t]; ok && val != f {
			return false
		}

		mapping1[f] = t
		mapping2[t] = f
	}

	return true
}
