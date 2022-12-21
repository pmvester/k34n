#!/bin/bash
influx delete --org k34 \
	      --bucket k34db \
	      --start '2022-10-16T15:24:04Z' \
	      --stop '2022-10-16T15:24:05Z' \
	      --predicate '_measurement="garage"'
