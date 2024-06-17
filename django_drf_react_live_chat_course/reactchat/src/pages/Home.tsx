import { Box, CssBaseline } from "@mui/material";

import { Main, PrimaryAppBar, PrimaryDraw, SecondaryDraw } from "./templates";

const Home = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <PrimaryAppBar />
      <PrimaryDraw children={undefined} />
      <SecondaryDraw />
      <Main />
    </Box>
  );
};

export default Home;
