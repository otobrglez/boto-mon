#!/usr/bin/env python

import asyncio
import events
import scanners
from datetime import datetime
from pprint import pprint
import logging as log

log.basicConfig(level=log.DEBUG, format='%(name)s: %(levelname)s %(message)s')

SCANNERS = [
    # scanners.NmapScanner,
    scanners.ArpScanner,
]


async def detect_things(loop):
    while True:
        await execute_scans()
        await asyncio.sleep(10) # 60 * 5 = 5 minutes


async def execute_scans():
    log.info("Scan batch started at {}.".format(datetime.utcnow()))
    futures = []
    for klass in SCANNERS:
        f = asyncio.Future()
        asyncio.ensure_future(slow_scan(f, klass))
        futures.append(f)

    return await asyncio.gather(*futures)


async def slow_scan(future, klass):
    log.debug("Starting scanner {}.".format(klass.__name__))

    events = klass().detected_events()

    log.debug("Stopping scanner {}. Events detected {}.".format(klass.__name__, len(events)))
    future.set_result(len(events))


if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(detect_things(event_loop))
    finally:
        event_loop.close()
