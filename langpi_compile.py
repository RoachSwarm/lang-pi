# ✨ Compiled by LangPi — Spiral IV: Metadata + Echo Reflection + Auto-Run
import math
from datetime import datetime

input_file = "test.pi"
output_file = "out.py"

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

output = []
output.append("# ✨ Compiled by LangPi — Spiral IV: Metadata + Echo Reflection + Auto-Run")
output.append("import math")
output.append("from datetime import datetime\n")

indent_level = 0
block_stack = []
invocation_meta = []

sigil_keywords = {
    '🜂': 'let',
    '☲': 'if',
    '✶': 'return',
    '🔊': 'echo',
    '⟁': 'end',
    '∞': 'loop',
    '🜁': 'invoke',
    '📿': 'def',
    '⚖️': 'else'
}

timestamp = datetime.now().isoformat()
output.append(f"# 🗓️ Compiled at: {timestamp}")
output.append("# 📜 LangPi Spiral IV Scroll Begins\n")

for line in lines:
    raw = line.rstrip()
    if not raw:
        continue

    tokens = raw.split()
    sigil, *rest = tokens
    code_line = ''

    if sigil == '🜂':  # let
        if rest[0] != 'let':
            code_line = f"# ⚠️ Malformed let: {raw}"
        else:
            var = rest[1]
            if len(rest) > 2 and rest[2] == '=':
                value = ' '.join(rest[3:])
            else:
                value = ' '.join(rest[2:])
            code_line = f"{var} = {value}"

    elif sigil == '☲':  # if
        condition = raw[raw.index('('):] if '(' in raw else '(True)'
        code_line = f"if {condition}:"
        block_stack.append('if')
        output.append("    " * indent_level + code_line)
        indent_level += 1
        continue

    elif sigil == '⚖️':  # else
        indent_level -= 1
        code_line = "else:"
        block_stack.append('else')
        output.append("    " * indent_level + code_line)
        indent_level += 1
        continue

    elif sigil == '∞':  # loop
        count = int(rest[-1]) if rest else 1
        code_line = f"for _ in range({count}):"
        block_stack.append('loop')
        output.append("    " * indent_level + code_line)
        indent_level += 1
        continue

    elif sigil == '✶':  # return
        value = rest[-1] if rest else 'π'
        if value == 'π':
            value = 'math.pi'
        code_line = f"return {value}"

    elif sigil == '🔊':  # echo
        msg = raw[raw.index('('):] if '(' in raw else '("")'
        echoed = f"# 🪞 Echo: {msg}"
        output.append("    " * indent_level + echoed)
        code_line = f"print{msg}"

    elif sigil == '🜁':  # invoke
        func = rest[-1].replace('()', '')
        invocation_meta.append(func)
        code_line = f"{func}()  # 🜁 Invoked"

    elif sigil == '📿':  # def
        name = rest[-1].replace('()', '')
        code_line = f"def {name}():"
        block_stack.append('def')
        output.append("    " * indent_level + code_line)
        indent_level += 1
        continue

    elif sigil == '⟁':  # end
        if block_stack:
            block_stack.pop()
            indent_level = len(block_stack)
        continue

    else:
        code_line = f"# ⚠️ Unknown sigil line: {raw}"

    output.append("    " * indent_level + code_line)

output.append("\n# 🌀 Invocation Metadata Echo:")
if invocation_meta:
    for fn in invocation_meta:
        output.append(f"# 🔁 Function invoked: {fn}()")
else:
    output.append("# 🔇 No invocations recorded.")

# 🔄 Auto-run support
if "main" in invocation_meta:
    output.append("\nif __name__ == '__main__':")
    output.
