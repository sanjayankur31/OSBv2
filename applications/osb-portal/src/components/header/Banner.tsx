import * as React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import Button from "@material-ui/core/Button";
import { UserInfo } from "../../types/user";

const useStyles = makeStyles((theme) => ({
  mainFeaturedPost: {
    position: "relative",
    backgroundImage: "url(images/banner.png)",
    backgroundSize: "cover",
    backgroundRepeat: "no-repeat",
    backgroundPosition: "center",
    height: "35vh",
  },
  mainFeaturedPostContent: {
    position: "absolute",
    bottom: 0,
    right: 0,
    left: 0,
    top: 0,
    backgroundColor: "rgba(0,0,0,.3)",
    display: "flex",
    alignItems: "flex-end",
    padding: theme.spacing(3),
  },
}));

export const Banner = (props: any) => {
  const classes = useStyles();
  const user: UserInfo = props.user;
  const handleSignup = () => {
    props.register();
  };

  const text1 =
    user === null ? "Welcome to the Open Source Brain v2.0 preview" : `Welcome back ${user.firstName}`;
  const text2 =
    user === null
      ? "Coming soon with NeuroML model creation, NWB data exploration and interactive development sessions."
      : "Let's do some science.";

  return (
    <Box className={classes.mainFeaturedPost}>
      <Box className={classes.mainFeaturedPostContent}>
        <Box>
          <Typography component="h2" variant="h1" gutterBottom={true}>
            {text1}
          </Typography>
          <Typography variant="subtitle1" paragraph={true}>
            {text2}
          </Typography>
          <Box display="flex" pt={1} flexDirection="row">
            {'' && // TODO temporarily disabled
              <Button variant="outlined">Take the tour</Button>
            }
            {user === null ? (
              <Button variant="outlined" onClick={handleSignup}>Sign up</Button>
            ) : null}
          </Box>
        </Box>
      </Box>
    </Box>
  );
};
