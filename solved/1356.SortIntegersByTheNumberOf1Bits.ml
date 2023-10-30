let to_bin a =
  let rec to_bin a res =
    match a with
      | 0 -> '0' :: res
      | 1 -> '1' :: res
      | n when (n mod 2) = 1 -> (to_bin [@tailcall]) (a/2) ('1' :: res)
      | n -> (to_bin [@tailcall]) (a/2) ('0' :: res)
  in to_bin a [];;

let count_ones list =
  let rec count_ones list res =
    match list with
      | [] -> res
      | h :: tail ->
        if h = '1'
          then (count_ones [@tailcall]) tail (res+1)
          else (count_ones [@tailcall]) tail res
  in count_ones list 0;;

let custom_compare a b =
  let a_ones = count_ones (to_bin a)
  and b_ones = count_ones (to_bin b)
  in match ((compare [@tailcall]) a_ones b_ones) with
    | 0 -> ((compare [@tailcall]) a b)
    | _ -> ((compare [@tailcall]) a_ones b_ones);;

let sort list = List.sort custom_compare list;;

sort [0;1;2;3;4;5;6;7;8];;
sort [1024;512;256;128;64;32;16;8;4;2;1];;

