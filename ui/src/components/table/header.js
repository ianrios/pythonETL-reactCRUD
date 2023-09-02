import TableHead from "@mui/material/TableHead";
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
            {column.label}
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
};

export default Header;
