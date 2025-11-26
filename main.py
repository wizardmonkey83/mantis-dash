from pymem import Pymem

pm = Pymem('GeometryDash.exe')
print(f"Process ID: {pm.process_id}")
address = pm.allocate(10)
base_address = pm.base_address
print(f"Base Address: {base_address}")
pm.write_int(address, 1337)
value = pm.read_int(address)
print(f"Allocated Value: {value}")
pm.free(address)