# SPDX-License-Identifier: BSD-2-Clause

# RTEMS Tools Project (http://www.rtems.org/)
# Copyright (C) 2020-2024 Amar Takhar <amar@rtems.org>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import pytest

from rtemstoolkit import config
from rtemstoolkit import macros
from rtemstoolkit import options


def test_config(rt_topdir):
    defaults = '%s/rtemstoolkit/defaults.mc' % (rt_topdir)

    long_opts = {
        # key              macro        handler   param  defs   init
        '--file': ('_file', 'path', True, None, False)
    }
    opts = options.command_line(base_path=rt_topdir,
                                argv=[
                                    "rtemstoolkit/config.py", "--file",
                                    "%s/tester/rtems/version.cfg" % rt_topdir
                                ],
                                defaults=macros.macros(name=defaults,
                                                       rtdir=rt_topdir),
                                long_opts=long_opts)

    options.load(opts)
    s = config.file(opts.defaults['_file'], opts)
    s.load(opts.defaults['_file'])
