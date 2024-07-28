"""
文件操作相关 util
"""

# coding = utf8


def load_text_line_file(filepath):
    with open(filepath) as ins:
        lines = ins.readlines()
        return lines


def dump_text_line_file(texts, filepath):
    with open(filepath, 'w') as outs:
        for t in texts:
            outs.write(t + '\n')
