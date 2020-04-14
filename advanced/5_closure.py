
def my_closure_function(capitalise_flag=False):
    # free variables bound to specific value enclosed in function scope
    prefix = ':start:'
    suffix = ':end:'

    def make_string(my_string):                 # the closures function
        a_string = my_string.capitalize() if capitalise_flag else my_string
        # make_string has everything it needs from closure object
        return prefix + a_string + suffix
    # we can tag with an attribute so we can inspect the closure later
    make_string.capitalise_flag = capitalise_flag
    return make_string                          # returns a function


print("can create a callable closure function object that has various values baked into it...")
# creates the closure object incorporating free variables/parameters
closure = my_closure_function(True)
print(closure.capitalise_flag)
# function doesn't need to specify prefix, suffix etc.. each time
print(closure('hello'))
# closure function object has 'capitalise' set to False
closure = my_closure_function(False)
print(closure.capitalise_flag)
print(closure('yellow'))


# if your filter function for filter() takes some other fixed parameters you can create a closure for it
# lower and upper parameters are stored in closure object
def create_reduction_filter(lower, upper):
    def apply_filter(x):                         # no free variables in this example
        return lower < x < upper
    return apply_filter


print("closures can be used with filter() when the reducing function needs extra parameters to perform reduction...")
# reduction filter that has multiple parameters
filter_5_9 = create_reduction_filter(5, 9)
# pass a list of numbers to the filter
print(list(filter(filter_5_9, list(range(0, 10)))))


def my_lambda_closure_function(capitalise_flag=False):
    prefix = ':start:'
    suffix = ':end:'
    # bake 3 variables into lambda
    return lambda x: prefix + (x.capitalize() if capitalise_flag else x) + suffix


print("we can return a lambda when we create the closure...")
closure = my_lambda_closure_function(True)
print(closure('hello'))
closure = my_lambda_closure_function(False)
print(closure('yellow'))
