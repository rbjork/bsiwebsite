CREATE TABLE countyparcels_simp
(
  "FIP" character varying(7) NOT NULL,
  "STATE" character varying(3),
  "COUNTY" character varying(50),
  "VERSION" character varying(16),
  "COMP" numeric,
  "APNPercent" character varying(15),
  "SITPercent" character varying(15),
  "OWNPercent" character varying(15),
  "USEPercent" character varying(15),
  "VALPercent" character varying(15),
  "STATUS" character varying(20),
  CONSTRAINT countyparcels_simp_pkey PRIMARY KEY ("FIP")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE countyparcels_simp
  OWNER TO postgres;
