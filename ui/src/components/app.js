import { Container } from "@mui/material";
import StatsTable from "./stats-table";
import VirtualTable from "./virtual-table";
import { useEffect, useState } from "react";
import { axiosHelper } from "../utils/axios-helper";

const App = () => {

  const [rows, setRows] = useState(0)
  const [pages, setPages] = useState(0)

  // get pages and rows for future use
  useEffect(() => {
    const url = 'covid-stats/pages'
    axiosHelper({
      url, successMethod: d => {
        setRows(d.data.row_count)
        setPages(d.data.max_pages)
      }
    })
  }, [])

  console.log({ rows, pages })

  return (
    <Container maxWidth="xl" sx={{ marginTop: '30px' }}>
      {/* <StatsTable /> */}
      <VirtualTable />
    </Container>
  );
}

export default App;
