from sympy import Matrix


class MachineMatrix(Matrix):
    """Matrix subclass adding custom methods and more readable repr & str"""

    def __new__(cls, rows: tuple[tuple[int | float]]):
        return super().__new__(cls, rows)

    def __repr__(self) -> str:
        return str(tuple(tuple(self.row(r)) for r in range(self.rows)))

    def __str__(self) -> str:
        return "\n".join([str(tuple(self.row(r))) for r in range(self.rows)])

    @classmethod
    def from_matrix(cls, matrix: Matrix) -> MachineMatrix:
        return cls(tuple(tuple(matrix.row(r)) for r in range(matrix.rows)))

    @property
    def lhs(self) -> MachineMatrix:
        lhs_matrix = MachineMatrix(tuple(tuple(self.row(r)) for r in range(self.rows)))
        lhs_matrix.col_del(lhs_matrix.cols - 1)
        return lhs_matrix

    @property
    def rhs(self) -> tuple:
        return tuple(self.col(self.cols - 1))

    def remove_zero_rows(self) -> None:
        while self.rows > 0 and set(self.row(self.rows - 1)) == {0}:
            self.row_del(self.rows - 1)
