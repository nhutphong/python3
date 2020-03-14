Kali linux:
cài = file.deb:
sudo dpkg --force-depends -i <ten file>
dpkg -i <ten file>

cài từ file .gz .....:
./configure (bash configure)
make
make install

khi cài software thiếu module thì chạy lệnh dưới:
apt --fix-broken install

apt-get clean -> dọn cache(file lưu tạm)
apt-get update --fix-missing
apt update && apt full-upgrade
apt-get install -f
kali linux login loop fix: login ko vào đc
Ctrl + Alt + F1/F2

dpkg --configure -a
apt-get dist-upgrade (khi upgrade ko upgrade được)
apt-get update
apt-get upgrade


sau khi upgrade
apt-get autoremove (xóa soft cũ)
apt-get purge <ten soft> (xóa soft)

chỉnh sữa sources.list để update & upgrade rất quan trọng
/etc/apt/sources.list

sữa grub:
fsck -yf </đường dẫn ổ đĩa>
fsck -f /
update-grub

root vlc:
sed -i s/geteuid/getppid/g /usr/bin/vlc

root google chrome:
terminal> gedit /opt/google/chrome/google-chrome
thêm : --user-data-dir  --no-sandbox

lsmod | grep blue
systemctl enable bluetooth.service
systemctl start bluetooth.service

/nholamgi/

apt-cache search <soft cần tìm>: tìm software
Git : khi dùng git nó sẽ download về /root/
qmake && make : để cài source tải về từ Git
*   = tất cả,
.    = thư mục đang việc trong terminal,
..   = thư mục cha của thư mục đang làm việc
;    = chạy được nhiều lệnh trong terminal
&& = nếu lệnh trước đúng thì chạy lệnh kế tiếp
||     = lệnh trước sai có thể chạy lệnh kế tiếp
{1..9} = chạy từ 1 tới 9 (khoảng) dùng cho tất cả touch, cat, mkdir...
[1-9] = chạy từ 1 tới 9 chỉ dùng xem (cat, ...)
[1,3,5] = có 1 hoặc 3 hoặc 5
~    =   /root
echo “Hello Kali linux” > file_name : cho nội dung và file_name
man <cd> : tìm cấu trúc lệnh cho cd
xman  :   software xem cấu trúc lệnh terminal
top : xem ứng dụng đang chạy (ram, cpu …)
w :
ps <option> : xem ứng đụng đang chạy
kill <pid=number> : tắt ứng dụng đang chạy
fdisk -l : xem ổ cứng trên computer
locate -i --limit 10 *.conf : tìm 10 file .conf
find </path/> : tìm folder và show cắc thành phần bên trong
find < *.txt > : show <path> file cần tìm

Tạo usb boot trên linux:
    1. fdisk -l : xác định /path/usb:
    2. dd if=<name.iso> of=</path/usb bs=512k

Tạo file và thư mục:
Touch {a..z}_{1..9}/file{1..100}: tạo nhiều file một lúc(vd: file1, file2… file100) trong chuỗi thư mục
mkdir {a..z}_{1..9}: tạo nhiều thư mục 1 lúc (vd: a_1, a_2, a_3, b_1, … z_9)
mkdir -p </dir/.../dir1>: tạo được đường dẫn thư mục dir1

Xóa file và thư mục:
rm < /file/ > : mắc định chỉ xóa file
rmdir < /folder/ > : chỉ xóa thư mục rỗng
rm *.txt: xóa tất cả file có đuôi txt ( *= tất cả)
rm *[2, 3]* xóa file có chứa số 2 hoặc 3
rm -r <folder>: xóa tất cả(thêm -r xóa được folder)
rm -ri <folder>: xác nhận các thư mục, file con cần xóa

Copy và di chuyển file và folder:
cp file1 file2 dich/ : copy thư file1 và file2 và folder dich
cp dich/* .    : copy tất cả trong thư mục dich ra thư mục đang làm việc (.)
cp -r : thêm -r để copy được thư mục
mv ~/Documents/Folder_mv ./Newname : di chuyển Folder_mv về thư mục hiện hành và đổi tền thành Newname

xem file:
cat file[1-5].txt : xem nội dung 5 file trong terminal
cat file[1-5].txt | tac(rev) : tac = từ 5-1, rev = đảo ngược nội dung của 5 file

tìm kiếm nội dung trong file:
sort < file > [option] | tac(less...) : sắp xếp nội dung file chữ hoặc số
grep [option] “content” file.* : highlight content trong file, đếm số lần xuất hiện của content …..
wc : điếm số từ


nén và giải nén:
file <file> : xem property của file
tar [option] <name.tar> <file.cần nén ….> : nén thành name.tar(option : f luôn đứng cuối)
    1. thêm option: z → nén thành name.tar.gz ( hoặc untar)
    2. thêm option: j → nén thành name.tar.bz2 ( hoặc untar)
    3. thêm option: v → xem nội dung trong file nén( terminal)

zip <name.zip> <file.cần nén …> : nén file
unzip <name.zip> : giải nén

gzip <name.tar>: nén thành name.tar.gz
gunzip <name.tar.gz> : giải nén thành name.tar

bzip2 <name.tar> : nén thành name.tar.bz2

tạo file script: name.sh
    1. trong file name.sh phải có:   #!/bin/bash = /usr/bin/python3
    2. Chạy name.sh : bash name.sh

Network:
traceroute <website> : Địa chỉ ip

GIT:
git add *
git commit -m ‘comment’

git push origin master            => ket noi account github
git remote add origin <ten-server>
