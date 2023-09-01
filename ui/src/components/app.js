import { Container } from "@mui/material";
import StatsTable from "./stats-table";
import VirtualTable from "./virtual-table";

const App = () => {
  return (
    <Container maxWidth="xl" sx={{ marginTop: '30px' }}>
      {/* <StatsTable /> */}
      <VirtualTable />
    </Container>
  );
}

export default App;
