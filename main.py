#!/usr/bin/env python
# coding=utf-8

import argparse
from src.remove import delete_directory, clear_directory, delete_file_pattern


def main(args):
    """
    different cases for to do actions
    """
    if args.action == 'rm_dir':
        delete_directory()
    elif args.action == 'clear_dir':
        clear_directory()
    elif args.action == 'rm_file':
        pass
    elif args.action == 'rm_ftype':
        delete_file_pattern()
    elif args.action == 'zip_dir':
        pass
    else:
        ValueError ("Parameter arg {} is not valid.".format(args.action))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Files - Directories Management')
    parser.add_argument('--action', type=str, dest='action', choices = ['rm_dir', 'clear_dir', 'rm_file', 'rm_ftype', 'zip_dir'], help='Action to do', required=True)
    #parser.add_argument('--zipname', type=str, dest='zipname', help='Zip name', default='test.zip')
    args = parser.parse_args()
    main(args)