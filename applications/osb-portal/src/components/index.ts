import { connect } from 'react-redux'

import { App as app } from '../App'
import { Workspaces as workspace } from './workspace/Workspaces'
import { WorkspaceToolBox as workspacetoolbox } from './workspace/NewWorkspaceToolBox'
import workspaceInteractions from './workspace/drawer/WorkspaceInteractions';

import { Banner as banner } from './header/Banner'
import { Header as header } from './header/Header'
import { WorkspaceDrawer as workspacedrawer } from './workspace/drawer/WorkspaceDrawer'
import { ErrorDialog as errorDialog } from './error-dialog/ErrorDialog'
import { WorkspaceFrame as workspaceFrame } from './workspace/WorkspaceFrame';
import { ProtectedRoute as protectedRoute } from './auth/ProtectedRouter';
import workspacePage from "../pages/WorkspacePage";

import { RootState } from '../store/rootReducer'
import * as WorkspacesActions from '../store/actions/workspaces'
import { userLogin, userLogout, userRegister } from '../store/actions/user';
import { toggleDrawer } from '../store/actions/drawer';
import { setError } from '../store/actions/error';
import newWorkspaceAskUser from './workspace/NewWorkspaceAskUser';
import { AnyAction, Dispatch } from 'redux';

import { RepositoryPage as repositoryPage } from '../pages/RepositoryPage'
import { RepositoriesPage as repositoriesPage } from '../pages/RepositoriesPage'

const mapWorkspacesStateToProps = (state: RootState) => {
  return ({
    showPublic: state.workspaces?.showPublic,
    publicWorkspaces: state.workspaces?.publicWorkspaces,
    userWorkspaces: state.workspaces?.userWorkspaces,
    user: state.user
  })
};

const mapSelectedWorkspaceStateToProps = (state: RootState) => ({
  workspace: state.workspaces?.selectedWorkspace,
  user: state.user,

});

const dispatchWorkspaceProps = {
  login: userLogin,
  logout: userLogout,
  ...WorkspacesActions
};

const mapUserStateToProps = (state: RootState) => ({
  user: state.user,
});

const dispatchUserProps = {
  login: userLogin,
  logout: userLogout,
  register: userRegister
};

const mapDrawerStateToProps = (state: RootState) => ({
  drawer: state.drawer,
});

const dispatchDrawerProps = {
  onToggleDrawer: toggleDrawer,
  ...WorkspacesActions
};

const mapErrorStateToProps = (state: RootState) => ({
  error: state.error,
});

const dispatchErrorProps = {
  setError
};

export const Workspaces = connect(mapWorkspacesStateToProps, dispatchWorkspaceProps)(workspace)
export const WorkspaceToolBox = connect(mapUserStateToProps, dispatchWorkspaceProps)(workspacetoolbox)
export const Banner = connect(mapUserStateToProps, dispatchUserProps)(banner)
export const Header = connect(mapUserStateToProps, { ...dispatchUserProps, ...dispatchDrawerProps })(header)
export const WorkspaceDrawer = connect(mapSelectedWorkspaceStateToProps, dispatchDrawerProps)(workspacedrawer) as any // any to fix weird type mapping error
export const WorkspaceInteractions = connect(mapSelectedWorkspaceStateToProps, dispatchWorkspaceProps)(workspaceInteractions) as any

export const App = connect(mapWorkspacesStateToProps, dispatchWorkspaceProps)(app)
export const ErrorDialog = connect(mapErrorStateToProps, dispatchErrorProps)(errorDialog)
const genericDispatch = (dispatch: Dispatch) => ({ dispatch: (action: AnyAction) => dispatch(action) });
export const WorkspaceFrame = connect(mapSelectedWorkspaceStateToProps, genericDispatch)(workspaceFrame)
export const WorkspacePage = connect(null, dispatchWorkspaceProps)(workspacePage);
export const RepositoryPage = connect(mapUserStateToProps)(repositoryPage)
export const RepositoriesPage = connect(mapUserStateToProps, null)(repositoriesPage)
export const NewWorkspaceAskUser = connect(null, dispatchUserProps)(newWorkspaceAskUser)
export const ProtectedRoute = connect(mapUserStateToProps, dispatchUserProps)(protectedRoute)
