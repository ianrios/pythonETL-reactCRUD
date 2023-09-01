import TableBody from "@mui/material/TableBody";
import TableRow from "@mui/material/TableRow";
import TableCell from "@mui/material/TableCell";
import { useAppContext } from "../../context/app-context";

const Body = () => {
  const { columns, currentPagedData, limit } = useAppContext();

  const emptyRows =
    page > 0 ? Math.max(0, (1 + page) * limit - currentPagedData.length) : 0;

  return (
    <TableBody>
      {currentPagedData
        .slice(page * limit, page * limit + limit)
        .map((row, index) => {
          const labelId = `enhanced-table-checkbox-${index}`;
          return (
            <TableRow hover role="checkbox" tabIndex={-1} key={index}>
              {columns.map((c, i) => (
                <TableCell
                  key={i}
                  component="th"
                  id={labelId}
                  scope="row"
                  padding="normal"
                >
                  {row[c.id]}
                </TableCell>
              ))}
            </TableRow>
          );
        })}
      {emptyRows > 0 && (
        <TableRow style={{ height: 53 * emptyRows }}>
          <TableCell colSpan={6} />
        </TableRow>
      )}
    </TableBody>
  );
};

export default Body;
