ALTER TABLE "Counties" 
ALTER COLUMN "COMP" TYPE numeric USING CAST("COMP" as numeric),
ALTER COLUMN "APNPercent" TYPE numeric USING CAST("APNPercent" as numeric),
ALTER COLUMN "SITPercent" TYPE numeric USING CAST("SITPercent" as numeric),
ALTER COLUMN "OWNPercent" TYPE numeric USING CAST("OWNPercent" as numeric),
ALTER COLUMN "USEPercent" TYPE numeric USING CAST("USEPercent" as numeric),
ALTER COLUMN "VALPercent" TYPE numeric USING CAST("VALPercent" as numeric),
ALTER COLUMN "FLRPercent" TYPE numeric USING CAST("FLRPercent" as numeric),
ALTER COLUMN "UNTPercent" TYPE numeric USING CAST("UNTPercent" as numeric),
ALTER COLUMN "YRBPercent" TYPE numeric USING CAST("YRBPercent" as numeric)