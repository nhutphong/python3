def checkPhone(num):
    if len(num) != 12:
        return False
    elif not num[:4].isalnum():
        return False
    elif num[4:5] != '-':
        return False
    elif not num[5:8].isalnum():
        return False
    elif num[8:9] != '-':
        return False
    elif not num[9:12].isalnum():
        return False
    return True


def nhapPhone():
    num = input('nhap sdt can kiem tra :')
    while not checkPhone(num):
        num = input('SAI!! vui long nhap lai sdt: ')
    else:
        print(f'Number Phone cua ban: {num}')


def main():
    nhapPhone()


if __name__ == '__main__':
    main()
