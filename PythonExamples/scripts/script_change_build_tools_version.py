#!/bin/usr/env python
# -*- coding: utf-8 -*-

'change buildToolsVersion for projects in Android Studio'

__author__ = 'sunxiaoling'

import os
import re
import logging
logging.basicConfig(level=logging.INFO)

r_include = re.compile(r'^include\s{1}\':(.*):(.*)\'$')
r_build_tools_version = re.compile(r'\s*buildToolsVersion\s{1}\'(.*)\'')

def change_build_tools_version(*args):
	logging.debug('*args: %s len: %d' % (args, len(args)))
	root_path = ''
	new_version = ''
	if len(args) >= 2:
		root_path = args[1]
		new_version = args[2]
	logging.debug('root_path: %s new_version: %s' % (root_path, new_version))
			
	if root_path == (None or ''):
		root_path = '.'
	if new_version == (None or ''):
		new_version = '22.0.1'
	logging.debug('root_path: %s new_version: %s' % (root_path, new_version))
	 
	setting_path = os.path.join(root_path, 'settings.gradle')
	logging.debug('setting_path: %s' % setting_path)
	include_projects = get_match_lines(setting_path, r_include)
	logging.debug(include_projects)
	for project in include_projects[1]:
		p_path = construct_project_path(project, root_path)
		file_path = os.path.join(p_path, 'build.gradle')
		logging.info(file_path)
		try:
			change_version(file_path, new_version)
		except IOError:
			logging.debug('IOERROR')

def get_match_lines(file_path, r):
	lines = []
	match_results = []
	with open(file_path, 'r') as f:
		while True:
			line = f.readline()
			logging.debug('readline:%s' % line)
			if len(line) == 0:
				break;
			match_result = r.match(line)
			logging.debug('line: %s match result: %s' % (line, match_result))
			if match_result:
				lines.append(line)
				match_results.append(match_result)
		return (lines, match_results)

def construct_project_path(project, root_path):
	p_path = root_path
	for s in project.groups():
		if s != '':
			p_path = os.path.join(p_path, s)
	logging.debug('p_path: %s' % p_path)
	return p_path
                    
def change_version(file_path, new_ver):
	matchs = get_match_lines(file_path, r_build_tools_version)
	logging.info(matchs)
	match_lines = matchs[0]
	match_results = matchs[1]
	if len(match_lines) == 0 or len(match_results) == 0:
		logging.info('----match failed!!\n')
		return
	ver_line = match_lines[0]
	ver_match = match_results[0]
	ver = ver_match.groups()[0]
	logging.info('ver:%s ver_line:%s' % (ver, ver_line))
	if ver != new_ver:
		c = ''
		new_c = ''
		try:
			fr = open(file_path, 'r')
			c = fr.read()
			if ver_line in c:
				new_ver_line = ver_line.replace(ver, new_ver)
				logging.info('new_ver_line:%s' % new_ver_line)
				new_c = c.replace(ver_line, new_ver_line)
		finally:
			fr.close()
			logging.debug('c:%s new_c:%s' % (c, new_c))
		if len(new_c) != 0:
			try:
				fw = open(file_path, 'w')
				fw.write(new_c)
				logging.info('----change version in (%s) success!!\n' % file_path)
			finally:
				fw.close()
	
if __name__ == '__main__':
	change_build_tools_version()