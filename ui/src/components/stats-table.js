import Paper from "@mui/material/Paper";
import Box from "@mui/material/Box";
import TableContainer from "@mui/material/TableContainer";
import Table from "@mui/material/Table";

import Toolbar from "./table/toolbar";
import Header from "./table/header";
import Body from "./table/body";
import Pagination from "./table/pagination";

import { useAppContext } from "../context/app-context";

const StatsTable = () => {
  const { columns, currentPagedData } = useAppContext();

  return (
    <Box>
      {columns.length && currentPagedData.length ? (
        <Paper>
          <Toolbar />
          <TableContainer style={{ maxHeight: "calc(100vh - 180px)" }}>
            <Table stickyHeader>
              <Header />
              <Body />
            </Table>
          </TableContainer>
          <Pagination />
        </Paper>
      ) : null}
    </Box>
  );
};

export default StatsTable;
