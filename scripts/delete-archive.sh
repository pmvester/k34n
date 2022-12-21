#!/bin/bash
influx delete --org k34 \
	      --bucket k34db \
	      --start '2022-12-04T22:02:02Z' \
	      --stop '2022-12-04T22:02:03Z' \
	      --predicate '_measurement="archive"'
