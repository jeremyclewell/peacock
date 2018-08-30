#!/usr/bin/env python -u
# encoding: utf-8

import fileinput
import os
import sys
import time

from watchdog.observers import Observer

from .events import PeacockEventHandler
from .syntax import DataHighlighter
from .log import log

# Unbuffered I/O not allowed on Python 3
# See http://bugs.python.org/issue11633 for conversation
if sys.version_info <= (3, 0) and type(sys.stdout) == 'file':
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

def outputlines(fi):
    highlight = DataHighlighter()
    try:
        if (fi == '-' or fi == sys.stdin):
            fi = sys.stdin
            while 1:
                try:
                    line = fi.readline()
                    if line:
                        sys.stdout.write(highlight.highlight_line(line))
                except KeyboardInterrupt:
                    break
        else:
            for line in fi:
                sys.stdout.write(highlight.highlight_line(line))

    except IOError as e:
        log.error(e)
        quit()

def watch_output(event):
    print(("\n==> %s <==" % os.path.basename(event.src_path)))
    outputlines(fileinput.input(event.src_path))

def monitor():

    fi = fileinput.input(sys.argv[1:], bufsize=1)
    paths = fi._files
    log.info("Using FILEINPUT with WATCHDOG for files: %s" % (', '.join(paths),))

    event_handler = PeacockEventHandler([os.path.abspath(p) for p in paths], watch_output)

    observer = Observer()
    recursive = False

    for p in paths:
        if p == '-' or p == sys.stdin:
            log.error("Can't mix stdin with file arguments. Quitting.")
            quit()
        else:
            if os.path.isdir(p):
                log.info("Watching directory '%s'" % p)
                recursive = True
            else:
                log.info("Will schedule file '%s'" % p)
                recursive = False
            p = os.path.dirname(os.path.abspath(p)) # Watchdog doesn't notify of file changes?
            observer.schedule(event_handler, path=p, recursive=recursive)

    observer.start()
    try:
        while True:
            time.sleep(0.125)
    except KeyboardInterrupt:
        observer.stop()
        quit()
    observer.join()
