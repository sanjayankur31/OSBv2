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

import { exists, mapValues } from '../runtime';
import {
    GITRepositoryResourceAllOf,
    GITRepositoryResourceAllOfFromJSON,
    GITRepositoryResourceAllOfFromJSONTyped,
    GITRepositoryResourceAllOfToJSON,
    RepositoryResourceBase,
    RepositoryResourceBaseFromJSON,
    RepositoryResourceBaseFromJSONTyped,
    RepositoryResourceBaseToJSON,
} from './';

/**
 * github repository resource
 * @export
 * @interface GITRepositoryResource
 */
export interface GITRepositoryResource {
    /**
     * file name
     * @type {string}
     * @memberof GITRepositoryResource
     */
    name?: string;
    /**
     * Download URL of the Resource
     * @type {string}
     * @memberof GITRepositoryResource
     */
    path?: string;
    /**
     * OSB Repository id
     * @type {number}
     * @memberof GITRepositoryResource
     */
    osbrepositoryId?: number;
    /**
     * The GIT ref
     * @type {string}
     * @memberof GITRepositoryResource
     */
    ref?: string;
    /**
     * The GIT sha of the resource
     * @type {string}
     * @memberof GITRepositoryResource
     */
    sha?: string;
}

export function GITRepositoryResourceFromJSON(json: any): GITRepositoryResource {
    return GITRepositoryResourceFromJSONTyped(json, false);
}

export function GITRepositoryResourceFromJSONTyped(json: any, ignoreDiscriminator: boolean): GITRepositoryResource {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'name': !exists(json, 'name') ? undefined : json['name'],
        'path': !exists(json, 'path') ? undefined : json['path'],
        'osbrepositoryId': !exists(json, 'osbrepository_id') ? undefined : json['osbrepository_id'],
        'ref': !exists(json, 'ref') ? undefined : json['ref'],
        'sha': !exists(json, 'sha') ? undefined : json['sha'],
    };
}

export function GITRepositoryResourceToJSON(value?: GITRepositoryResource | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'name': value.name,
        'path': value.path,
        'osbrepository_id': value.osbrepositoryId,
        'ref': value.ref,
        'sha': value.sha,
    };
}


