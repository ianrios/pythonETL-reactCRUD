import TableHead from "@mui/material/TableHead";
import TableSortLabel from "@mui/material/TableSortLabel";
import { TableCell, TableRow } from "@mui/material";

import { useAppContext } from "../../context/app-context";

const Header = () => {
  const { columns } = useAppContext();

  // commented out filter data from MUI - not very useful for a table this small that is getting all its data from the backend
  // TODO: create filter methods for the backend queries

  return (
    <TableHead>
      <TableRow>
        {columns.map((column, i) => (
          <TableCell key={i} align={"left"} padding="normal">
            <TableSortLabel>{column.label}</TableSortLabel>
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
};

export default Header;
