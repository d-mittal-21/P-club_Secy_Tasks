import angr
import claripy
success_address = 0x0000177b
failure_address = 0x0000178f
base_address = 0x000001b4
flag_length = 30
project = angr.Project("./rev", main_opts={"base_addr": base_address})
flag_chars = [claripy.BVS(f"flag_char{i}", 8) for i in range(flag_length)]
flag = claripy.Concat(*flag_chars + [claripy.BVV(b"\n")])

state = project.factory.full_init_state(
    args=['./rev'],
    add_options=angr.options.unicorn,
    stdin=flag,
)
for k in flag_chars:
    state.solver.add(k >= ord('!'))
    state.solver.add(k <= ord('-'))

simgr = project.factory.simulation_manager(state)
simgr.explore(find=success_address, avoid=failure_address)
if len(simgr.found) > 0:
    for found in simgr.found:
        print(found.posix.dumps(0))
