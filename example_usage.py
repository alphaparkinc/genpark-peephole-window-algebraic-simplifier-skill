from client import PeepholeSimplifier

def main():
    print("=== Testing Peephole Algebraic Simplifier ===")
    peep = PeepholeSimplifier()

    raw_code = [
        "ADD r1, 0",
        "MUL r2, 2",
        "MOV r3, r3",
        "ADD r4, 10"
    ]
    print("Raw assembly instructions:", raw_code)
    opt_code = peep.optimize(raw_code)
    print("Optimized assembly instructions:", opt_code)

    assert opt_code == ["SHL r2, 1", "ADD r4, 10"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
