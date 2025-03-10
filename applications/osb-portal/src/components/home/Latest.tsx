import * as React from "react";

import { makeStyles } from "@material-ui/core/styles";
import { Typography, Box, Link } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  paper: {
    padding: theme.spacing(2),
    margin: theme.spacing(1),
    textAlign: "left",
  },
  partners: {

    fontSize: "0.9em",
    marginBottom: "0.5em",
  }
}));

export const Latest = () => {
  const classes = useStyles();

  return (
    <Box display="flex" flexDirection="column" className="verticalFill">
      <Typography component="h2" variant="h6" gutterBottom={true}>
        Disclaimer
     </Typography>
      <Box mt={3} flexGrow="1"  >
        <Typography>
          This is a beta release of version 2.0 of the Open Source Brain platform, which is under active development and testing.
        </Typography>
        <br />
        <Typography>
          <strong>User accounts, data and workspaces are subject to change without notice.</strong>
        </Typography>
        <br />
        <Typography>
          For now please use the live <Link href="http://opensourcebrain.org">OSBv1 platform</Link>, <Link href="http://nwbexplorer.opensourcebrain.org">NWB Explorer</Link> or <Link href="http://netpyne.opensourcebrain.org">NetPyNE</Link>.

          Please <Link href="http://opensourcebrain.org/docs#How_To_Contact_Us">get in contact</Link> if you would like to help with user testing.
        </Typography>

      </Box>

      <Box alignSelf="flex-end" justifySelf="flex-end" alignItems="center" textAlign="right">
        <Typography className={classes.partners}>

          Supported by
        </Typography>
        <Link href="https://wellcome.org" target="_blank"><img alt="Wellcome" title="Wellcome" src="/images/wellcome.png" width="50" /></Link>
      </Box>
      {/* <Typography component="h2" variant="h6" gutterBottom={true}>
        Latest
      </Typography>
      <Box mt={3}>
        <Typography>
          20/03/2021 - OSB Meeting announced, yes still Hotel Calabona
        </Typography>
        <Typography>20/03/2023 - NeuroML 6 released</Typography>
        <Typography>20/03/2041 - C. elegans fully simulated!</Typography>
      </Box> */}
    </Box>
  );
};
