UPDATE countyparcels_counties
SET "FIP" = lpad(trim("FIP"),5,'0'),
"COMP" = substring("COMP" from '\d+'),
"APNPercent" = substring("APNPercent" from '\d+'),
"SITPercent" = substring("SITPercent" from '\d+'), 
"OWNPercent" = substring("OWNPercent" from '\d+'),
"USEPercent" = substring("USEPercent" from '\d+'), 
"VALPercent" = substring("VALPercent" from '\d+'),
"FLRPercent" = substring("FLRPercent" from '\d+'), 
"UNTPercent" = substring("UNTPercent" from '\d+'),
"YRBPercent" = substring("YRBPercent" from '\d+') 
