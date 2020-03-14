import os
import send2trash
import shutil #copy-move-delete_files-dirs
import zipfile


print("xin chao python")
os.path.join('folder1','folder2','file.png') => string : đường dẫn file them
'/'

os.chdir('C:\\') => string : thấy đổi thư mục làm việc hiện tại
os.getcwd() => string : đường dẫn thư mục làm việc
os.walk('.') => ('root/', [dirs,...], [files,...]), (), ... =>
generator cac tuple => root, dirs, files = list(os.walk('.'))[0]
os.listdir(path) => list: [folders, files, ...] trong
current working directory

os.path.abspath('file.png') => string : '/folderworking/' + '/' + 'file.png'|'folder' => fullpath file.py dang chay
os.path.abspath(__file__) = os.path.realpath(__file__)

os.path.isabs('..\\..\\file.png') = False
os.path.isabs('c:\\folder\\folder') =True
os.path.relpath('/root/Videos', '/root/code/python')
=> string '../../Videos'
os.path.dirname('c:\\folder1\\folder2\\file.png')
=> string = 'c:\\folder1\\folder2\\'
os.path.basename('c:\\folder1\\folder2\\file.png')
=> string = 'file.png' đường dẫn file cuối cùng or thư mục cuối
os.path.exists('c:\\folder1\\folder2\\file.png') => True or False
=> sự tồn tại của file and folder
os.path.isfile('c:\\folder1\\folder2\\file.png')
=> True or False có phải là file hay không
os.path.isdir('path') True or False : có phải là đường dẫn hay không
os.path.getsize('path//file.png') str số byte của file
os.mkdir('path/to/folder') => create a dir
os.rmdir('path/to/folder') => delete dir=folder => only delete dir empty
os.mknod("new_file")
os.unlink('path/to/file')  => delete file

shutil.copy('c:\\spam.txt','e:\\tailieu\\spam.txt') => copy file sang e:\\
shutil.copytree('c:\\delicious','e:\\delicious_backup') => copy thư mục
shutil.move('c:\\spam.txt','e:\\tailieu') => spam.txt rename => tailieu
shutil.move('c:\\spam.txt','e:\\tailieu\\nhut.txt') => cut qua tailieu đổi tên nhut.txt
shutil.rmtree('c:\\delicious') => xóa thư mục

send2trash.send2trash('') => di chuyển thư mục or file tới thùng rác
