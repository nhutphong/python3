import math

print('tao la run.py')

print([math.sqrt(i) for i in range(5)])

def action():
    return "tao la action() thuoc run.py"


# pyscript.write('element_id', 'value') # element_id bat buoc
# pyscript.write('element_id', action())


pyscript.write('run', action())

name = 'nguyen thong dung'
info = {key: value for key, value in enumerate(name, 1)}
pyscript.write('compreshension', info)