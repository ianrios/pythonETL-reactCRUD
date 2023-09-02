import { Box, IconButton, TablePagination, useTheme } from "@mui/material";

import FirstPageIcon from '@mui/icons-material/FirstPage';
import KeyboardArrowLeft from '@mui/icons-material/KeyboardArrowLeft';
import KeyboardArrowRight from '@mui/icons-material/KeyboardArrowRight';
import LastPageIcon from '@mui/icons-material/LastPage';

import { useAppContext } from "../../context/app-context";



function TablePaginationActions(props) {
  const theme = useTheme();
  const { count, page, rowsPerPage, onPageChange } = props;

  const handleFirstPageButtonClick = (event) => {
    onPageChange('first');
  };

  const handleBackButtonClick = (event) => {
    onPageChange('prev');
  };

  const handleNextButtonClick = (event) => {
    onPageChange('next');
  };

  const handleLastPageButtonClick = (event) => {
    onPageChange('last');
  };

  return (
    <Box sx={{ flexShrink: 0, ml: 2.5 }}>
      <IconButton
        onClick={handleFirstPageButtonClick}
        disabled={page === 0}
        aria-label="first page"
      >
        {theme.direction === 'rtl' ? <LastPageIcon /> : <FirstPageIcon />}
      </IconButton>
      <IconButton
        onClick={handleBackButtonClick}
        disabled={page === 0}
        aria-label="previous page"
      >
        {theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
      </IconButton>
      <IconButton
        onClick={handleNextButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="next page"
      >
        {theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
      </IconButton>
      <IconButton
        onClick={handleLastPageButtonClick}
        disabled={page >= Math.ceil(count / rowsPerPage) - 1}
        aria-label="last page"
      >
        {theme.direction === 'rtl' ? <FirstPageIcon /> : <LastPageIcon />}
      </IconButton>
    </Box>
  );
}

const Pagination = () => {
  const {
    rows,
    limitsArr,
    limit,
    setNewLimit,
    page,
    getPage,
    totalAvailablePages,
  } = useAppContext();

  const handleChangePageReducer = (nextState) => {
    switch (nextState) {
      case 'first':
        getPage({ page: 0 })
        break;
      case 'prev':
        getPage({ page: page - 1 })
        break;
      case 'next':
        getPage({ page: page + 1 })
        break;
      case 'last':
        getPage({ page: totalAvailablePages })
        break;
      default:
        console.log("didn't match any case")
        break;
    }
  }

  const handleChangeRowsPerPage = (event) => {
    setNewLimit(parseInt(event.target.value, 10))
  };

  return (
    <TablePagination
      rowsPerPageOptions={limitsArr} // TODO: add { label: 'All', value: -1 } when i add virtualization
      colSpan={3}
      component="div"
      count={rows}
      rowsPerPage={limit}
      page={page}
      SelectProps={{
        inputProps: {
          'aria-label': 'rows per page',
        },
        native: true,
      }}
      onPageChange={handleChangePageReducer}
      onRowsPerPageChange={handleChangeRowsPerPage}
      ActionsComponent={TablePaginationActions}
    />
  );
};

export default Pagination;
