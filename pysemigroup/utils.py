import os
import tempfile
import webbrowser
import pickle

tmp = []

GraphVizExt = ["bmp",
"canon",
"dot",
"gv",
"xdot",
"xdot1.2",
"xdot1.4",
"cgimage",
"cmap",
"eps",
"exr",
"fig",
"gd",
"gd2",
"gif",
"gtk",
"ico",
"imap",
"cmapx",
"imap_np",
"cmapx_np",
"ismap",
"jp2",
"jpg",
"jpeg",
"jpe",
"json",
"json0",
"dot_json",
"xdot_json",
"pct",
"pict",
"pdf",
"pic",
"plain",
"plain-ext",
"png",
"pov",
"ps",
"ps2",
"psd",
"sgi",
"svg",
"svgz",
"tga",
"tif",
"tiff",
"tk",
"vml",
"vmlz",
"vrml",
"wbmp",
"webp",
"xlib",
"x11"]


def save_graphviz(graphviz_str, filename, extension=None, directory=None, verbose=False):
    (fd, file_dot) = tempfile.mkstemp(suffix=".dot",
                                      dir=directory)
    file_out = filename
    l = file_out.split(".")
    if extension is None:
        extension = l[len(l) - 1]
    if extension not in GraphVizExt:
        raise ValueError("Not a valid Graphviz output format")
    f = open(fd, "w")
    f.write(graphviz_str)
    f.close()
    compil = 'dot -T{} {} -o {}'.format(extension,
                                        file_dot,
                                        file_out)
    if verbose:
        print("Graphviz Compilation:", compil)
    os.system(compil)


def view_graphviz(graphviz_str, save_to_file=None, extension="svg", directory=None, verbose=False):
    if save_to_file is None:
        (fd, file_svg) = tempfile.mkstemp(suffix="." + extension,
                                          dir=directory)
        open(fd).close()
    else:
        file_svg = save_to_file
    save_graphviz(graphviz_str, file_svg,
                  extension=extension,
                  directory=directory,
                  verbose=verbose)
    webbrowser.open(file_svg)


def delete_file(s):
    os.system('rm %s' % s)


def save(obj, file_name):
    with open(file_name, "wb") as f:
        pickle.dump(obj, f)


def load(file_name):
    with open(file_name, "rb") as f:
        obj = pickle.load(f)
    return obj


def gcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)
