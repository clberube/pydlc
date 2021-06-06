# @Author: charles
# @Date:   2021-06-06 09:06:59
# @Email:  charles.berube@polymtl.ca
# @Last modified by:   charles
# @Last modified time: 2021-06-06 09:06:98


from distutils.core import setup
setup(
  name = 'pydlc',         # How you named your package folder (MyLib)
  packages = ['pydlc'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python implementation of the Density Line Chart (Moritz & Fisher, 2018) to visualize large collections of time series.',   # Give a short description about your library
  author = 'Charles L. Bérubé',                   # Type in your name
  author_email = 'charles.berube@polymtl.ca',      # Type in your E-Mail
  url = 'https://github.com/clberube/pydlc',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/clberube/pydlc/archive/refs/tags/v0.1.tar.gz',    # I explain this later on
  keywords = ['data visualization', 'density', 'time series'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Science/Research',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)
