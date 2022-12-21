from(bucket: "k34db")
  |> range(start: -100d, stop: now())
  |> filter(fn: (r) =>
    r._measurement == "energy" and
    r._field == "energy"
  )
