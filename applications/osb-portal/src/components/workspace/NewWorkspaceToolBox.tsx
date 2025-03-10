import * as React from "react";

import { makeStyles } from "@material-ui/core/styles";
import { Typography, Grid, Paper } from "@material-ui/core";

import Box from "@material-ui/core/Box";


import "react-markdown-editor-lite/lib/index.css";

import { UserInfo } from "../../types/user";
import { ResourceType } from "../../types/global";

import WorkspaceItem, { WorkspaceTemplateType } from "./NewWorkspaceItem";

import * as Icons from '../icons';

const useStyles = makeStyles((theme) => ({
  iconButton: {
    width: "2em",
    height: "2em",
    padding: 0,
  },
  svgIcon: {},

  dialogButtons: {
    paddingRight: 0,
  },
  toolBoxHeading: {
    textAlign: "center",
    [theme.breakpoints.up("md")]: {
      textAlign: "left",
    },
  },
  justifyCenter: {
    justifyContent: 'center'
  },
  cardText: {
    display: "inline-block",
    marginRight: "5px",
    [theme.breakpoints.up("md")]: {
      display: "block",
      marginRight: "0",
    },
  },
}));



export const WorkspaceToolBox = (props: any) => {
  const classes = useStyles();

  const user: UserInfo = props.user;

  const type: string = props.type;

  return (
    <>

      <Box>
        <Grid container={true} alignItems="center" justify="center" spacing={5}>
          <Grid item={true} sm={12} md={4} lg={3}>
            <Typography component="h2" variant="h6" className={classes.toolBoxHeading}>
              <Box component="span" className={classes.cardText}>Create a</Box>
              <Box component="span" className={classes.cardText}>new Workspace</Box>
            </Typography>
          </Grid>
          <Grid item={true} xs={12} sm={12} md={8} lg={9}>
            <Grid container={true} direction="row" justify="space-between" spacing={5} >
              <Grid item={true} xs={12} sm={4} className={classes.justifyCenter} >
                <WorkspaceItem
                  icon={Icons.SquareCirclesIcon}
                  title="Computational modeling"
                  template={WorkspaceTemplateType.network}
                  user={user}
                  refreshWorkspaces={props.refreshWorkspaces}

                />
              </Grid>
              <Grid item={true} xs={12} sm={4} className={classes.justifyCenter}>
                <WorkspaceItem
                  icon={Icons.ChartIcon}
                  title="Data analysis"
                  template={WorkspaceTemplateType.explorer}
                  user={user}
                  refreshWorkspaces={props.refreshWorkspaces}
                />
              </Grid>
              <Grid item={true} xs={12} sm={4} className={classes.justifyCenter}>
                <WorkspaceItem
                  icon={Icons.CubeIcon}
                  title="Interactive development"
                  template={WorkspaceTemplateType.playground}
                  user={user}
                  refreshWorkspaces={props.refreshWorkspaces}
                />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Box>
    </>
  );
};
