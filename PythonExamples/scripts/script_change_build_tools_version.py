#!/bin/usr/env python
# -*- coding: utf-8 -*-

'change buildToolsVersion for projects in Android Studio'

__author__ = 'sunxiaoling'

import os
import re
import logging
logging.basicConfig(level=logging.INFO)

def change_build_tools_version(*args):
        logging.info('*args: %s len: %d' % (args, len(args)))
        root_path = ''
        new_version = ''
        if len(args) >= 2:
                root_path = args[1]
                new_version = args[2]
        logging.info('root_path: %s new_version: %s' % (root_path, new_version))
        
        if root_path == (None or ''):
                root_path = '.'
        if new_version == (None or ''):
                new_version = '22.0.1'
        logging.info('root_path: %s new_version: %s' % (root_path, new_version))
        
        r_include = re.compile(r'^include.*$')
        r_build_tools_version = re.compile(r'buildToolsVersion\s')
 
        setting_path = os.path.join(root_path, 'settings.gradle')
        logging.info('setting_path: %s' % setting_path)
        include_projects = get_match_lines(setting_path, r_include)
        logging.info(include_projects)
        for project in include_projects:
                p_path = construct_project_path(project, root_path)
                print p_path
                with open(p_path, 'r') as f:
                        content = f.read()
                        print content

def get_match_lines(file_path, r):
        lines = []
        with open(file_path, 'r') as f:
                line = f.readline()
                logging.info('first line: %s' % line)
                while len(line) != 0:
                        match_result = r.match(line)
                        logging.info('line: %s match result: %s' % (line, match_result))
                        if match_result:
                                lines.append(line)
                        line = f.readline()
                return lines

def construct_project_path(project, root_path):
        temp = project.split('\'')
        logging.info('----temp: %s' % temp)
        temp = temp[1].split(':')
        logging.info('----temp: %s' % temp)
        p_path = root_path
        for s in temp:
                if s != '':
                        p_path = os.path.join(p_path, s)
        logging.info('p_path: %s' % p_path)
        return p_path
                        
		
if __name__ == '__main__':
	change_build_tools_version()
