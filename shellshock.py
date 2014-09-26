# -*- mode: python; coding: utf-8 -*-

# Copyright 2014 Jeffrey C. Ollie
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil
import subprocess
import tempfile

def grains():
    result = {}

    # test for CVE-2014-6271

    bash = subprocess.Popen(['bash', '-c', 'echo this is a test'],
                            env = {'x': '() { :;}; echo vulnerable'},
                            stdin = None,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    bash.wait()

    result['shellshock1_stdout'] = bash.stdout.read()
    result['shellshock1_stderr'] = bash.stderr.read()
    
    if result['shellshock1_stdout'].find('vulnerable') >= 0:
        result['shellshock1'] = 'vulnerable'

    else:
        result['shellshock1'] = 'not vulnerable'

    # test for CVE-2014-7169

    tmpdir = tempfile.mkdtemp()

    result['shellshock2_tmpdir'] = tmpdir

    bash = subprocess.Popen(['bash', '-c', 'echo date'],
                            env = {'x': '() { (a)=>\\'},
                            cwd = tmpdir,
                            stdin = None,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    bash.wait()

    result['shellshock2_stdout'] = bash.stdout.read()
    result['shellshock2_stderr'] = bash.stderr.read()

    if os.path.exists(os.path.join(tmpdir, 'echo')):
        result['shellshock2'] = 'vulnerable'

    else:
        result['shellshock2'] = 'not vulnerable'

    shutil.rmtree(tmpdir)

    if result['shellshock1'] == 'vulnerable' or result['shellshock2'] == 'vulnerable':
        result['shellshock'] = 'vulnerable'

    else:
        result['shellshock'] = 'not vulnerable'

    return result

if __name__ == '__main__':
    print grains()
