from distutils.core import setup
setup(
  name = 'dbipyt',
  packages = ['dbipyt'],
  version = '0.1.2',
  license= 'MIT',
  description = 'API Wrapper for Discord Bot Index [GUILD COUNT POSTING, BOT INFO SEARCH]',
  author = 'Luke J',
  author_email = 'itsnotluke@outlook.com',
  url = 'https://github.com/LiquidBlast/discordbotindex-dbi-python',
  download_url = 'https://github.com/LiquidBlast/discordbotindex-dbi-python/archive/v_0.01.tar.gz',
  keywords = ['apiwrapper', 'dbi', 'discordbotindex'],
  install_requires=[
          'aiohttp',
          'json'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
