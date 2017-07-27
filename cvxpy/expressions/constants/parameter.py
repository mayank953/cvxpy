"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

from cvxpy import settings as s
from cvxpy.expressions.leaf import Leaf
import cvxpy.lin_ops.lin_utils as lu


class Parameter(Leaf):
    """
    A parameter, either matrix or scalar.
    """
    PARAM_COUNT = 0

    def __init__(self, rows=1, cols=1, name=None, sign="unknown", value=None):
        self.id = lu.get_id()
        self._rows = rows
        self._cols = cols
        self._sign_str = sign
        if name is None:
            self._name = "%s%d" % (s.PARAM_PREFIX, self.id)
        else:
            self._name = name
        # Initialize with value if provided.
        self._value = None
        if value is not None:
            self.value = value
        super(Parameter, self).__init__()

    def copy(self, args=None, id_objects={}):
        """Returns a shallow copy of the object.
        """
        if self.id in id_objects:
            return id_objects[self.id]
        if args is None:
            args = self.args
        data = self.get_data()
        if data is not None:
            new_obj = type(self)(*(args + data))
        else:
            new_obj = type(self)(*args)
        id_objects[self.id] = new_obj
        return new_obj

    def get_data(self):
        """Returns info needed to reconstruct the expression besides the args.
        """
        return [self._rows, self._cols, self._name, self._sign_str, self._value]

    def name(self):
        return self._name

    @property
    def shape(self):
        """Returns the (row, col) dimensions of the expression.
        """
        return (self._rows, self._cols)

    def is_positive(self):
        """Is the expression positive?
        """
        return self._sign_str == s.ZERO or self._sign_str.upper() == s.POSITIVE

    def is_negative(self):
        """Is the expression negative?
        """
        return self._sign_str == s.ZERO or self._sign_str.upper() == s.NEGATIVE

    def is_specified(self):
        """Has the parameter value been specified?
        """
        return self._value is not None

    # Getter and setter for parameter value.
    @property
    def value(self):
        if not self.is_specified():
            raise ValueError("Parameter value has not been specified.")
        return self._value

    @value.setter
    def value(self, val):
        self._value = self._validate_value(val)

    @property
    def grad(self):
        """Gives the (sub/super)gradient of the expression w.r.t. each variable.

        Matrix expressions are vectorized, so the gradient is a matrix.

        Returns:
            A map of variable to SciPy CSC sparse matrix or None.
        """
        return {}

    def parameters(self):
        """Returns itself as a parameter.
        """
        return [self]

    def canonicalize(self):
        """Returns the graph implementation of the object.

        Returns:
            A tuple of (affine expression, [constraints]).
        """
        obj = lu.create_param(self, self.shape)
        return (obj, [])

    def __repr__(self):
        """String to recreate the object.
        """
        return 'Parameter(%d, %d, sign="%s")' % (self._rows,
                                                 self._cols,
                                                 self.sign)
