import TableHead from "@mui/material/TableHead";
import TableSortLabel from "@mui/material/TableSortLabel";
import { TableCell, TableRow } from "@mui/material";

import { useAppContext } from "../../context/app-context";

const Header = () => {
  const { columns } = useAppContext();

  // TODO: create filter and sort methods for the backend queries with MUI components
  // may need to pass in specific filter by and sort by options to backend

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
