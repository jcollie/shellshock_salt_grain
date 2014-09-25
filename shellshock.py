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

import subprocess

def grains():
    bash = subprocess.Popen(['bash', '-c', 'echo this is a test'],
                            env={'x': '() { :;}; echo vulnerable'},
                            stdin = None,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE)
    bash.wait()

    result = {'shellshock_stdout': bash.stdout.read(),
              'shellshock_stderr': bash.stderr.read()}
    
    if result['shellshock_stdout'].find('vulnerable') >= 0:
        result['shellshock'] = 'vulnerable'

    else:
        result['shellshock'] = 'not vulnerable'

    return result
