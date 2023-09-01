import { TablePagination } from "@mui/material";
import React, { useState } from "react";
import { useAppContext } from "../../context/app-context";

const Pagination = () => {
  const { rows, limitsArr, limit, setNewLimit } = useAppContext();

  const [page, setPage] = useState(0);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setNewLimit(parseInt(event.target.value, 10));
    setPage(0);
  };

  return (
    <TablePagination
      rowsPerPageOptions={limitsArr}
      component="div"
      count={rows}
      rowsPerPage={limit}
      page={page}
      onPageChange={handleChangePage}
      onRowsPerPageChange={handleChangeRowsPerPage}
    />
  );
};

export default Pagination;
