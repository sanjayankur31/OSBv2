import os

from cloudharness import log
from cloudharness.events.client import EventClient
from flask import current_app

import workspaces.repository.model_repository as repos

DOWNLOAD_FILE_QUEUE = "osb-download-file-queue"
UPDATE_WORKSPACES_RESOURCE_QUEUE = "osb-update-workspace-resources"


def _create_topic(name):
    client = EventClient(name)
    try:
        client.create_topic()
    except:
        log.info(f"Queue {name} already exists!")
        pass
    return client


def update_workspace_resources(event_client, app, message):
    log.info(f"Got message: {message}")
    workspace_id = message["workspace_id"]
    # remove /project_download/ (mount point of the pvc) from the path
    resources = [resource.replace("/project_download/", "") for resource in message["resources"]]
    with app.app_context():
        repos.WorkspaceResourceRepository().update_workspace_resources(workspace_id, resources)


_consumer_clients = []
_consumer_queues = (
    {"group": "workspaces", "name": UPDATE_WORKSPACES_RESOURCE_QUEUE, "handler": update_workspace_resources},
)


def start_kafka_consumers():
    log.info("Starting Kafka consumer threads")
    for queue in _consumer_queues:
        client = _create_topic(queue["name"])
        client.async_consume(app=current_app, group_id=queue["group"], handler=queue["handler"])
        _consumer_clients.append(client)


def stop_kafka_consumers():
    log.info("Stopping Kafka consumer threads")
    for t in _consumer_clients:
        t.close()
        log.info(f"Stopped Kafka consumer thread: {t}")


def test_kafka_running():
    try:
        EventClient("mnp-workspaces-testing")._get_consumer()
    except:
        return False
    return True
