import subprocess
import tempfile
import os

def runPython(code):
    result = subprocess.run(
        ["python3", "-c", code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout or result.stderr

def runNode(code):
    result = subprocess.run(
        ["node","-e",code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout or result.stderr

def runJava(code):
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "Main.java")

        with open(file_path, "w") as f:
            f.write(code)

        # compile
        compile = subprocess.run(
            ["javac", file_path],
            capture_output=True,
            text=True
        )

        if compile.stderr:
            return compile.stderr

        # run
        run = subprocess.run(
            ["java", "-cp", tmpdir, "Main"],
            capture_output=True,
            text=True,
            timeout=5
        )

        return run.stdout or run.stderr
    

def runC(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".c") as f:
        f.write(code.encode())
        file_path = f.name

    exe_path = file_path.replace(".c", "")

    compile = subprocess.run(
        ["gcc", file_path, "-o", exe_path],
        capture_output=True,
        text=True
    )

    if compile.stderr:
        return compile.stderr

    run = subprocess.run(
        [exe_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return run.stdout or run.stderr


def runCpp(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".cpp") as f:
        f.write(code.encode())
        file_path = f.name

    exe_path = file_path.replace(".cpp", "")

    compile = subprocess.run(
        ["g++", file_path, "-o", exe_path],
        capture_output=True,
        text=True
    )

    if compile.stderr:
        return compile.stderr

    run = subprocess.run(
        [exe_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return run.stdout or run.stderr


def runRuby(code):
    result = subprocess.run(
        ["ruby", "-e", code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout or result.stderr

def runGo(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".go") as f:
        f.write(code.encode())
        file_path = f.name

    run = subprocess.run(
        ["go", "run", file_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return run.stdout or run.stderr

def runPhp(code):
    result = subprocess.run(
        ["php", "-r", code],
        capture_output=True,
        text=True,
        timeout=5
    )
    return result.stdout or result.stderr

def runTypescript(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ts") as f:
        f.write(code.encode())
        file_path = f.name

    run = subprocess.run(
        ["ts-node", file_path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return run.stdout or run.stderr

def runCsharp(code):
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, "Program.cs")

        with open(file_path, "w") as f:
            f.write(code)

        # compile
        compile = subprocess.run(
            ["mcs", file_path],
            capture_output=True,
            text=True
        )

        if compile.stderr:
            return compile.stderr

        exe_path = file_path.replace(".cs", ".exe")

        run = subprocess.run(
            ["mono", exe_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        return run.stdout or run.stderr




