# Two decorator analogy
def split(fun):
    def inner(name):
        str1 = fun(name)+" I am your server "
        return str1

    return inner


def upper_every(fun):
    def function_Call(name):
        a = str("\x1B[3m")+fun(name)+"\x1B[0m"
        return a
    return function_Call


@split
@upper_every
def greating(name):
    return f"Hello {name.capitalize()} , I am your robot"


# rutvik = greating("rutvik")
# print(rutvik)


# If decorator has input


def outer(expre):
    def adding_info(fun):
        def inner(name, sname):
            s2 = fun(name, sname)+f" and ,This is our {expre} "
            return s2
        return inner

    return adding_info


@outer("decorator function")
def rutvik_greating(name, sname):
    return f"Hello {name} {sname}"


print(rutvik_greating("Rutvik", "Jaiswal"))
