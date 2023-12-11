from math_operations import basic_operations, power_operation, apply_operations

result_basic = basic_operations(10, 5)
print("Basic Operations Result:", result_basic)

result_power = power_operation(2, 3)
print("Power Operation Result:", result_power)

operations_list = [
    (basic_operations, (8, 4)),
    (power_operation, (3, 2)),
]

result_apply = apply_operations(operations_list)
print("Apply Operations Result:", result_apply)