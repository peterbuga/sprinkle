#!/usr/bin/env python3
"""
common utilities
"""
__author__ = "Michael Montuori [michael.montuori@gmail.com]"
__copyright__ = "Copyright 2017 Michael Montuori. All rights reserved."
__credits__ = []
__license__ = "closed"
__version__ = "0.1"
__revision__ = "2"

import subprocess
import os.path
import logging

def combine_jsons(json_str):
    return '[' + json_str.replace(']\n',',',json_str.count(']\n')-1).replace('||[\n','')

def is_file(file):
    if not os.path.isfile(file):
        return False
    else:
        return True

def is_dir(dir):
    if not os.path.isdir(dir):
        return False
    else:
        return True


def remove_localdir(local_dir, path):
    basedir = os.path.dirname(local_dir)
    return path.replace(basedir,'').replace('\\', '/')


def normalize_path(path):
    return path.replace('\\', '/')


def execute(command_with_args):
    logging.debug("Invoking : %s", " ".join(command_with_args))
    try:
        with subprocess.Popen(
                command_with_args,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE) as proc:
            (out, err) = proc.communicate()

            # out = proc.stdout.read()
            # err = proc.stderr.read()

            logging.debug(out)
            if err:
                logging.warning(err.decode("utf-8").replace("\\n", "\n"))

            return {
                "code": proc.returncode,
                "out": out.decode('utf-8'),
                "error": err.decode('utf-8')
            }
    except FileNotFoundError as not_found_e:
        logging.error("Executable not found. %s", not_found_e)
        return {
            "code": -20,
            "error": not_found_e
        }
    except Exception as generic_e:
        logging.exception("Error running command. Reason: %s", generic_e)
        return {
            "code": -30,
            "error": generic_e
        }


def print_line(line):
    print(line)