import { Container } from "@mui/material";

import StatsTable from "./stats-table";
import Table from "./table";
import VirtualTable from "./virtual-table";

import { useAppContext } from "../context/app-context";
import EnhancedTable from "./table";

const App = () => {

  const { rows, pages } = useAppContext()

  console.log({ rows, pages })


  return (
    <Container maxWidth="xl" sx={{ marginTop: '30px' }}>
      {/* <StatsTable /> */}
      {/* <Table /> */}
      {/* <VirtualTable /> */}
      <EnhancedTable />
    </Container>
  );
}

export default App;
