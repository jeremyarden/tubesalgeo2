PETUNJUK PENGGUNAAN 
1. Jalankan file executable program yang diinginkan, pilih 2d atau 3d.
2. Masukkan titik-titik berupa (x,y) sejumlah yang kamu inginkan untuk membentuk poligon,
   atau masukkan 8 titik berupa (x,y) untuk membentuk sebuah kubus.
3. Masukkan perintah yang kamu inginkan.
   Untuk 2 dimensi :
	translate <dx> <dy>   : menggeser nilai x dan y sebesar dx dan dy
	dilate <k>            : melakukan dilatasi objek dengan faktor scaling k
	rotate <deg> <a> <b>  : melakukan rotasi objek berlawanan arah jarum jam sebesar
							deg derajat terhadap titik a, b
	reflect <param>       : melakukan pencerminan objek, param bernilai x, y, y=x. y=-x,
							atau (a,b)
	shear <param> <k>     : melakukan operasi shear kepada objek, nilai param adalah x
							atau y, nilai k adalah faktor shear
	stretch <param> <k>   : melakukan operasi stretch kepada objek, nilai param adalah x
							atau y, nilai k adalah faktor stretch
	custom <a> <b> <c> <d>: melakukan transformasi linir kepada objek dengan matriks
							[[a,b],[c,d]]
	multiple <n>          : melakukan transformasi linier pada objek sebanyak n kali berurutan, 
	. . . //input 1         setiap baris input 1..n dapat berupa translate, rotate, shear, dll 
	. . . //input 2         tetapi bukan multiple, reset, exit
	. . .
	. . . //input n
	reset                 : mengembalikan objek pada kondisi awal objek didefinisikan
	exit                  : keluar dari program
   Untuk 3 dimensi :
	translate <dx> <dy> <dz>   : menggeser nilai x dan y sebesar dx dan dy
	dilate <k>            	   : melakukan dilatasi objek dengan faktor scaling k
	rotate <param> <deg>       : melakukan rotasi objek berlawanan arah jarum jam sebesar
							deg derajat terhadap sumbu x, y, atau z
	reflect <param>            : melakukan pencerminan objek, param bernilai xz, xy, atau yz
	shear <param> <k>          : melakukan operasi shear kepada objek, nilai param adalah x, y,
				     atau z, nilai k adalah faktor shear
	stretch <param> <k>   	   : melakukan operasi stretch kepada objek, nilai param adalah x, y,
				     atau z, nilai k adalah faktor stretch
	custom <a> <b> <c> <d> <e> <f> <g> <h> <i> : melakukan transformasi linir kepada objek dengan matriks
							[[a,b,c],[d,e,f],[g,h,i]]
	multiple <n>          : melakukan transformasi linier pada objek sebanyak n kali berurutan, 
	. . . //input 1         setiap baris input 1..n dapat berupa translate, rotate, shear, dll 
	. . . //input 2         tetapi bukan multiple, reset, exit
	. . .
	. . . //input n
	reset                 : mengembalikan objek pada kondisi awal objek didefinisikan
	exit                  : keluar dari program