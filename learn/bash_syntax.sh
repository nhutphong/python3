#! bin/bash

# nen dung -> ""

# int dung: (()), []
# if ((int,<,<=,>,>=)), if [-eq,-ne,-lt,le,-gt,-ge ]
# -o=or
# -a=and
# ! phu dinh

# muon +,-,*,/, %... phai co: let z=a*b or them $[5+3]
# string dung: [[]], []

# if [[string, <,>]], if [=, ==, !=]
# option: -z string la null
# -f: la file, -d: la directory
# if [-z $1] : neu param 1 khong ton tai thi run(condition)

echo 'Hello bash scripts'

echo BASH xin chao $BASH
echo BASH_VERSION xin chao $BASH_VERSION
echo HOME xin chao $HOME
echo PWD xin chao $PWD

name=Phong
old=25

echo ten ban la $name
echo tuoi ban la $old

# echo "enter names: "
# read name1 name2 name3 # input()
# echo "Names: $name1, $name2, $name3"
# $0=file_name, $1...$i=> cac params


echo $0, $1, $2, $3

# args=("$@")

# echo arg $@
# echo len $#

#array
# [a-z], [A-Z], [1-9] =>
# ? => ky tu dac biet
# * => tu 2 letter tro len

array=('thanh tan' 'thanh phong' 'ngoc hanh' 'dung cau')
# dung slice cho array and string => ${name[@]:1:3} => pos 1 lay 3 phan tu
# or ${name[*]:2} => tu pos 2 lay full_string
# @=*
echo "array_value_full: ${array[@]}"
echo "array_index_full: ${!array[@]}"
echo "array_len: ${#array[@]}"

declare -A arr_dict # bat buoc key&value
arr_dict=([nhut]="vo thanh phong" [tan]="nguyen thanh tan")
# unset array[2]

for i in ${!array[@]}; do
    echo $i: ${array[i]}
done

for i in {1..10..2}; do
    echo $i
done

num=1
while [ $num -le 5 ]; do
    echo $num
    ((num++))
done

for comm in ls cal date; do
    echo "===========================${comm}=========================="
    $comm
done

echo "pid is $$"
dirname: ${file_name%/*}
basename: ${file_name##*/}
echo {1..100..3}
{a..l..2}
{z..a..3}
seq 1 $1 => for i in  $(seq 1 3 $1) => chi dung cho int
name='vo thanh phong'
echo ${name,,} => lowercase
echo ${name^^} => uppercasek

=========================================================================

variable trong func la global=toan_cuc

change default shell=command:
chsh -s $(which bash)
chsh -s $(which zsh)

shift: tang vi tri param1 = value param2
value $1 bi mat di
$1 thanh $2
$2 thanh $3
loop: until nguoc lai voi while command1 false se chay do done;

gvim ~/. profile
export SHELL=/bin/bash
exec /bin/bash

export giong alias

`cmd`: important
'string', "string"
?: bat ky ky ru nao nhung chi 1 ky tu
$? = 0
[...]:
*: bat ky lay nhieu
$(seq 1 10)
[A-Za-z]: lam viec voi file and dir
[xyz]*: char bat dau = x or y or z
[!]: phu dinh
*[a-m4-7]: char end=[trong khoang da cho]
-z $1 : neu ko ton tai tham so $1
$0 -> file_name
$1..$9, ${10..} -> params cua func pa1 pa2 ...
$@ -> full params value
$# -> len(so params)
dirname: ${file_name%/*}
basename: ${file_name##*/}
var=nhut
temp=var, echo ${!var} => nhut
echo ${name:=zeze} => print zeze if name=null

IFS="," => split=cac chuoi

operator:
-a=&&
-o=||
read x
if [ $x == "Y" ] || [ $x == "y" ]
if [[ "$x" = "Y" || "$x" = "y" ]]
$((a +,-,*,/ b))
$[a +,-,*,/ b]


case esac:
;; break mac dinh
;& full ko quan trong dieu kien
;;& pattern

Create file:
touch file_name

redirection:
stdout_cmd nay la stdin_cmd kia
ls | grep 'phong' => stdout_ls la stdin_grep
ls 1>&0 grep 'phong'
cmd > file
cmd < file
cmd << string
0=    stdin>   => input or file_contents
1=    >stdout  => new_ file or source cho cmd
2=    stderr => thong bao loi
2>&1 => copy stderr vao stdout
1>&2 => copy stdout vao stderr
stdin > stdout or |
&> file_name => stdout and stderr vao file_name
>> file_name(append content)
cat  < name.txt
cmd stdin=source.txt < source.txt

open file in terminal:
cat: file_name_nho, show contents dau->end
tac: show contents end->dau
more: mo file_lon theo page
file:
less:  mo file trong terminal scroll tu tu
head: 10 dong dau
tail: print 10 lines cua file| tail: mo file, in 10 dong cuoi
nl: lines number => int
more: page number => %int

tim kiem:
wc file_name: dem so: <lines, words, chars>
wc -l < path_to_file=source
grep: tim kiem contents va highlight no trong filev
awk <-options> '{print $1}' => xu ly file text rat manh, la 1 ngon ngu lap trinh
sed 's/regex /g' stdin=file: find, replace,
 /g=replace, /d=delete

sap xep:
sort, ...,  trong file
sort:
cut -d "," -f 1 name.txt => remove comma(,) -> -f 1 la 1 tab
tr: replace text stdin => new_text stdout

tim kiem files and dirs
find <path,...,> <options> <contents>  => tim file trong dir
find path -name lulu\* => tim lulu...
-iname phu dinh
-regex, -iregex
-type <bcdpfls>
-mtime <+,- hour> +=sau24h, -=truoc24h
-size
find . -name \? -daystart -mtime +0 -mtime -3
locate <path to path>

so sanh contents file:
cmp <options>
diff file1 file2

network:
nc
nmap

set `cmd`: $1,$2... la stdout_cmd

split: chia nho file
cat file* > new_join_file

chmod 777 file_ name => full permission
chmod o+rwx,g+r data.txt
r=4, w=2, x=1
u=user, g=group, o=other(user con lai), a=all tat ca users
-r cam doc
+w cho phep ghi
x execute
chown -R user_name: group_name dir_name
-R => app dung lun cho files,dirs child

locate .bashrc => all vi tri file
trap [cmd] [SIGNALS]

/usr/bin
/bin
/etc
/etc/shells

====================================

TRASH:
sudo chown -R yourusername ~/.local/share/Trash/
rm -rf ~/.local/share/Trash

Shortcut root:
/usr/share/applications/

BOOT usb on ubuntu:
cp <file.iso> /dev/sdb
sync

Extensions:
preload tree

GIT:
git submodule update --init --recursive

PIP:
pip3 install -U --user pip
them: --user vao command pip

~/.bashrc
export PATH=$PATH:`pwd`/flutter/bin

name.sh
#!usr/bin/env python3
#!usr/bin/env bash
#!/bin/bash

google drive:
change url: uc => open

cài = file.deb:
sudo dpkg --force-depends -i <ten file>
dpkg -i < *.deb >

cài từ file .gz .....:
./configure
make
make install

khi cài software thiếu module thì chạy lệnh dưới:
sudo apt install --fix-broken --fix-missing

apt-get clean -> dọn cache(file lưu tạm)
apt-get update --fix-missing
apt update && apt full-upgrade
apt-get install -f
kali linux login loop fix: login ko vào đc
Ctrl + Alt + F2

lỗi dpkg:
setup cac package dang wait
dpkg --configure -a

apt-get upgrade
apt-get dist-upgrade

sau khi upgrade
apt-get autoremove (xóa soft cũ)
apt-get purge <ten soft> (xóa soft)

chỉnh sữa sources.list để update & upgrade rất quan trọng
/etc/apt/sources.list

sữa grub:
fsck -yf [/dev/sda1]
update-grub

deluser --remove-home <upssername>
useradd <username>
passwd <username>

root vlc:
sed -i s/geteuid/getppid/g /usr/bin/vlc
terminal: leafpad /opt/google/chrome/google-chrome
root chrome: --user-data-dir --no-sandbox

show version: grep VERSION /etc/os-release

unblock dpkg:
ps -aux | grep -i apt
kill -9 <process_id>

/root/.local/share/applications/  => thêm <name>.Desktop để hiện trên dash(search=win) để add vào dock

font: terminal: fc-cache trước khi thêm và sau khi xóa font

default app:
gedit /root/.config/mimeapps.list

systemctl enable bluetooth.service
systemctl start bluetooth.service

/nholamgi/
