# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
	#在此定义一些变量
    'var_name': 'vaule',
  },
  'targets': [
  	{
    'target_name': 'hello_jni_headers',
    'type': 'none',
    'sources': [
      'src/com/mx/example/hello_jni/Hello.java',
    ],
    'variables': {
      'jni_gen_dir': 'hello_jni',
    },
    'includes': [ '../../build/jni_generator.gypi' ],
  	},
  ],
}
