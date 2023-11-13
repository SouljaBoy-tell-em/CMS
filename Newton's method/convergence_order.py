import warnings
warnings.filterwarnings("ignore")

def InitY(block, null_eq):
    Y = list()
    for i in (block[2]):
        Y.append((np.log(abs(null_eq + i - block[0])))/(np.log(abs(null_eq - block[0]))))
        null_eq += i
    return Y


%matplotlib inline 
def CreateGraph(null_eq, case, axis_i):
    block = simple_newton_mod(func0, dfunc0, null_eq)
    print(f"{case}:\nsolve = {block[0]}\niterations = {block[1]}\n")
    Y = InitY(block, null_eq)
    axis_i.plot(range(len(Y)), Y)
    axis_i.set_title(case)

figure, axis = plt.subplots(2, 2) 
CreateGraph(8, 'case1', axis[0, 0])
CreateGraph(0.7, 'case2', axis[0, 1])
CreateGraph(0.0, 'case3', axis[1, 0])
