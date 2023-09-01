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
  const { columns, rows } = useAppContext();

  return (
    <Box>
      {columns.length && rows.length && (
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
      )}
    </Box>
  );
};

export default StatsTable;
