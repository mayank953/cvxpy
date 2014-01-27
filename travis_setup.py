from setuptools import setup

setup(
    name='cvxpy',
    version='0.1',
    author='Steven Diamond, Eric Chu, Stephen Boyd',
    author_email='stevend2@stanford.edu, echu508@stanford.edu, boyd@stanford.edu',
    packages=['cvxpy',
              'cvxpy.atoms',
              'cvxpy.atoms.affine',
              'cvxpy.atoms.elementwise',
              'cvxpy.constraints',
              'cvxpy.expressions',
              'cvxpy.expressions.constants',
              'cvxpy.expressions.variables',
              'cvxpy.interface',
              'cvxpy.interface.numpy_interface',
              'cvxpy.interface.cvxopt_interface',
              'cvxpy.problems',
              'cvxpy.tests',
              'cvxpy.utilities'],
    package_dir={'cvxpy': 'cvxpy'},
        url='http://github.com/cvxgrp/cvxpy/',
    license='...',
    description='A domain-specific language for modeling convex optimization problems in Python.',
    install_requires = ["ecos >= 1.0"]
)
