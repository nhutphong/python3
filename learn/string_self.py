a = "hoc Lap tRinh qua de   "
		nói về string
		s.lstrip('nhut') = > string = cắt('n,h,u,t') tu trai vao giua
		s.strip('phong') -> string = cắt('p,h,o,n,g') đứng liền nhau = > từ trái-phải vào giữa
		cắt tất cả chúng nếu các chữ đứng cạnh nhau nếu ngắc bị ngắc không cắt nữa, (chỉ đầu và cuối)
		s.rstrip() = > string = tu phai vao giua default = cat space(khoang trang)

		s.split(sep=None, maxsplit=-1) -> list = không có đối số là cắt khoảng trắng(string sau khi bị cắt sẽ chuyển về list)
		s.split(',') ->return list = cắt dấu phẩy ',' maxsplit=int(so la cat)
		s.rsplit() => right to left maxsplit=-1 la cat full
		trước tiên nên dùng s.split() để cắt khoảng trắng và chuyển về list
		','.join(['vo', 'Thanh', 'Phong']) = string 'vo,thanh,phong'
		s.replace('o', 'an',5) -> string = 'o' được thay thế bằng 'an' 5 lan

		s.lower() tất cả viết thường
		s.upper() tất cả viết hoa
		s.swapcase() thường thành hoa, hoa thành thường
		s.capitalize() -> string = viết HOA chữ cái đầu(của phần tử trong list or tuple)
		s.title() -> string = viết hoa chữ cái đầu của tất cả các từ trong chuỗi
		s.find('q') -> int = tìm ký tự 'q' trong chuỗi trả về vị trí của index của nó(không tìm thấy false: -1)
		s.rfind('q') -> int = tìm từ bên phải qua
		s.index('q') -> int = giống find nhưng ko tim thấy thì sài raise ValueError
		s.rindex('q') -> int = giống rfind nhưng ko tim thấy thì sài raise ValueError

        table = s.makestran('old', 'NEW') => dict{ord('o'): ord('N'), ord('l'): ord('E'), ...}
        my_name.translate(table) => se thay the 'o, l, d' = 'N, E, W' trong my_name

		s.center(width[, fillchar]) -> string = thêm kí tự fillchar vào 2 bên chuỗi, với dk width = độ dài
		s.rjust(width[, fillchar]) -> string = thêm fillchar vào bên trái
		s.ljust(width[, fillchar]) -> string = thêm fillchar vào bên phải

		True or False
		s.islower() = > True or False (tất cả viết thường)
		s.isupper() = > True or False (tất vả viết hoa)
		s.isalpha() = > trong a tất cả đều là chữ thì True, còn lại và thêm '', ' ' False
		s.numeric() = > trong a tất cả đều là số thì True, nêu có 1 chữ khác số thì False
		s.isalnum() = > chữ a-z hoặc 0-9 là True, còn lại False
		s.isspace() = > tất cả đều là khoảng trắng thì True, còn lại(cả '') là False
		còn nhiều
		s.startswith('y'[, start[, end]]) -> bool = kiểm tra từ đầu tiên trong chuỗi, đúng là True
		s.endswith('y'[, start[, end]]) -> bool = kiểm tra chữ cuối cùng trong chuỗi, đúng là True

		s.count('d') -> int = số lần xuất hiện trong chuỗi
		len(a) cho biết độ dài chuỗi
		range(1, 11, 3) khi đó chạy sẽ in ra là: 1, 4, 7, 10
		range(5, 0, -1) in ra: 5, 4, 3, 2, 1

 if i % 2 == 0 : continue -> bỏ qua các trường hợp thỏa mãng điều kiện này
	if i % 5 == 0 : break -> thoát vòng lặp khi thỏa mãng điều kiện này
visual code:

"[html]": {
        "editor.tabSize": 2
	},
"[javascript]": {
    "editor.tabSize": 2
  },
"[json]": {
    "editor.tabSize": 2
  },

"editor.wordWrap": "bounded",
    "editor.rulers": [80],
