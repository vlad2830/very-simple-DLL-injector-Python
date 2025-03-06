from pymem import Pymem
from pymem.process import inject_dll_from_path

dll_path = input("Enter the DLL PATH: ")
process_name = input("Enter the process name: ")

open_process = Pymem(process_name)
inject_dll_from_path(open_process.process_handle, dll_path)

print("DLL injected successfully")