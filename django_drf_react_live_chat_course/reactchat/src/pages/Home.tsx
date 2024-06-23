import { Box, CssBaseline } from "@mui/material";

import PopularChannels from "@components/PrimaryDraw/PopularChannels";
import { Main, PrimaryAppBar, PrimaryDraw, SecondaryDraw } from "./templates";

const Home = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <PrimaryAppBar />
      <PrimaryDraw>
        <PopularChannels open={false} />
      </PrimaryDraw>
      <SecondaryDraw />
      <Main />
    </Box>
  );
};

export default Home;
