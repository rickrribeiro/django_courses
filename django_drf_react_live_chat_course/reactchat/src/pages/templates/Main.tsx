import { Box, useTheme } from "@mui/material";
// import PrimaryAppBar from "./PrimaryAppBar";
// import PrimaryDraw from "./PrimaryDraw";
// import SecondaryDraw from "./SecondaryDraw";

const Main = () => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        flexGrow: 1,
        mt: `${theme.primaryAppBar.height}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        overflow: "hidden",
      }}
    >
      {/* <PrimaryAppBar />
      <PrimaryDraw />
      <SecondaryDraw /> */}
    </Box>
  );
};

export default Main;
