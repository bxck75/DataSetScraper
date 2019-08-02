# -*- coding: utf-8 -*-

from __future__ import print_function, division
import argparse
from os.path import join

import subprocess
from urllib.request import Request, urlopen

__author__ = 'Fisher Yu'
__email__ = 'fy@cs.princeton.edu'
__license__ = 'MIT'


def list_categories():
    # url = 'http://tigress-web.princeton.edu/~fy/lsun/public/release/'
    # with urlopen(Request(url)) as response:
    # return response.read().decode().strip().split('\n')
        return ['cow','boat','car','bus','dog','horse']


def download(out_dir, category, set_name):
    url = 'http://tigress-web.princeton.edu/~fy/lsun/public/release/' \
          '{set_name}.zip'.format(**locals())
    # if set_name == 'test':
    #     out_name = 'test.zip'
    #     # url = 'http://dl.yf.io/lsun/scenes/{set_name}_lmdb.zip'
    #     url = 'http://tigress-web.princeton.edu/~fy/lsun/public/release/{set_name}.zip'
    # else:
    print(url)
    out_name = '{category}_{set_name}.zip'.format(**locals())
    out_path = join(out_dir, out_name)
    cmd = ['wget', url]
    print('Downloading', category, set_name, 'set')
    subprocess.call(cmd)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out_dir', default='')
    parser.add_argument('-c', '--category', default=None)
    args = parser.parse_args()

    categories = list_categories()
    if args.category is None:
        print('Downloading', len(categories), 'categories')
        for category in categories:
            download(args.out_dir, category, 'train')
            download(args.out_dir, category, 'val')
        download(args.out_dir, '', 'test')
    else:
        if args.category == 'test':
            download(args.out_dir, '', 'test')
        elif args.category not in categories:
            print(categories)
            print('Error:', args.category, "doesn't exist in", 'LSUN release')
        else:
            download(args.out_dir, args.category, 'train')
            download(args.out_dir, args.category, 'val')


if __name__ == '__main__':
    main()
