CREATE TABLE "County"
(
  "FIP" character(7) NOT NULL,
  "STATE" character(4),
  "COUNTY" character(50),
  "VERSION" character(16),
  "COMP" character(4),
  "APNPercent" character(4),
  "SITPercent" character(4),
  "OWNPercent" character(4),
  "USEPercent" character(4),
  "VALPercent" character(4),
  "FLRPercent" character(4),
  "UNTPercent" character(4),
  "YRBPercent" character(4)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "County"
  OWNER TO postgres;