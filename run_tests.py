import sys, subprocess

if len(sys.argv) == 2:
    common_name = sys.argv[1]
    for i in range(2):
        name = f"{sys.argv[1]}{i}"
        out_file = open(f"{name}.out")
        out_content = (out_file.read())
        
        wynik = subprocess.run(
            ["python", f"{common_name}.py", f"{name}"], 
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        output = wynik.stdout
        # print(wynik)
        print(f"output == out_content: {output == out_content}, output: {output}, out_content: {out_content}")
        out_file.close()

else:
    print("Run like this: 'python run_tests.py <common_part_for_file_and_tests_name>'")


