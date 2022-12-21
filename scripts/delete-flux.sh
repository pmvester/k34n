#!/bin/bash
influx delete --org k34 \
	      --bucket k34db \
	      --start '2022-07-26T09:02:44Z' \
	      --stop '2022-07-26T09:02:45Z' \
	      --predicate '_measurement="outdoor"'
