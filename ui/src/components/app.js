import { Container } from "@mui/material";

import StatsTable from "./stats-table";

const App = () => {
  return (
    <Container maxWidth="xl" sx={{ marginTop: "30px" }}>
      <StatsTable />
    </Container>
  );
};

export default App;
