class PeepholeSimplifier:
    """
    Peephole Optimization Sliding Window.
    Applies strength reduction and algebraic identities:
    - ADD x, 0 -> eliminated
    - MUL x, 2 -> SHL x, 1
    - MOV x, x -> eliminated
    """
    def optimize(self, instructions):
        opt = []
        for instr in instructions:
            parts = instr.replace(',', '').split()
            op = parts[0]
            if op == "ADD" and parts[2] == "0":
                continue
            elif op == "MOV" and parts[1] == parts[2]:
                continue
            elif op == "MUL" and parts[2] == "2":
                opt.append(f"SHL {parts[1]}, 1")
            else:
                opt.append(instr)
        return opt
