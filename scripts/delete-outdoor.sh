#!/bin/bash
influx delete --org k34 \
	      --bucket k34db \
	      --start '2022-12-11T16:12:33Z' \
	      --stop '2022-12-11T16:12:34Z' \
	      --predicate '_measurement="outdoor"'
