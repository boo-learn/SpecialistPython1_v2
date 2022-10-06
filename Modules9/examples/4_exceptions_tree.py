import inspect
# our treeClass function
def treeClass(cls, ind=0):
    # print name of the class
    print('-' * ind, cls.__name__)

    # iterating through subclasses
    for i in cls.__subclasses__():
        treeClass(i, ind + 3)


print("Hierarchy for Built-in exceptions is : ")

# inspect.getmro() Return a tuple
# of class  cls’s base classes.

# building a tree hierarchy
inspect.getclasstree(inspect.getmro(BaseException))

# function call
treeClass(BaseException)

# BaseException
# --- Exception
# ------ TypeError
# ------ StopAsyncIteration
# ------ StopIteration
# ------ ImportError
# --------- ModuleNotFoundError
# --------- ZipImportError
# ------ OSError
# --------- ConnectionError
# ------------ BrokenPipeError
# ------------ ConnectionAbortedError
# ------------ ConnectionRefusedError
# ------------ ConnectionResetError
# --------- BlockingIOError
# --------- ChildProcessError
# --------- FileExistsError
# --------- FileNotFoundError
# --------- IsADirectoryError
# --------- NotADirectoryError
# --------- InterruptedError
# --------- PermissionError
# --------- ProcessLookupError
# --------- TimeoutError
# --------- UnsupportedOperation
# ------ EOFError
# ------ RuntimeError
# --------- RecursionError
# --------- NotImplementedError
# --------- _DeadlockError
# ------ NameError
# --------- UnboundLocalError
# ------ AttributeError
# ------ SyntaxError
# --------- IndentationError
# ------------ TabError
# ------ LookupError
# --------- IndexError
# --------- KeyError
# --------- CodecRegistryError
# ------ ValueError
# --------- UnicodeError
# ------------ UnicodeEncodeError
# ------------ UnicodeDecodeError
# ------------ UnicodeTranslateError
# --------- UnsupportedOperation
# ------ AssertionError
# ------ ArithmeticError
# --------- FloatingPointError
# --------- OverflowError
# --------- ZeroDivisionError
# ------ SystemError
# --------- CodecRegistryError
# ------ ReferenceError
# ------ MemoryError
# ------ BufferError
# ------ Warning
# --------- UserWarning
# --------- DeprecationWarning
# --------- PendingDeprecationWarning
# --------- SyntaxWarning
# --------- RuntimeWarning
# --------- FutureWarning
# --------- ImportWarning
# --------- UnicodeWarning
# --------- BytesWarning
# --------- ResourceWarning
# ------ _OptionError
# ------ error
# ------ Verbose
# ------ Error
# ------ TokenError
# ------ StopTokenizing
# ------ EndOfBlock
# --- GeneratorExit
# --- SystemExit
# --- KeyboardInterrupt
