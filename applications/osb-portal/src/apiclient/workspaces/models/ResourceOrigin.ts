/* tslint:disable */
/* eslint-disable */
/**
 * Workspaces manager API
 * Opensource Brain Platform - Reference Workspaces manager API
 *
 * The version of the OpenAPI document: 0.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import {
    DownloadResource,
    RepositoryResource,
    DownloadResourceFromJSONTyped,
    DownloadResourceToJSON,
    RepositoryResourceFromJSONTyped,
    RepositoryResourceToJSON,
} from './';

/**
 * @type ResourceOrigin
 * optional Resource where the WorkspaceResource is build from
 * @export
 */
export type ResourceOrigin = DownloadResource | RepositoryResource;

export function ResourceOriginFromJSON(json: any): ResourceOrigin {
    return ResourceOriginFromJSONTyped(json, false);
}

export function ResourceOriginFromJSONTyped(json: any, ignoreDiscriminator: boolean): ResourceOrigin {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return { ...DownloadResourceFromJSONTyped(json, true), ...RepositoryResourceFromJSONTyped(json, true) };
}

export function ResourceOriginToJSON(value?: ResourceOrigin | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return { ...DownloadResourceToJSON(value), ...RepositoryResourceToJSON(value) };
}

