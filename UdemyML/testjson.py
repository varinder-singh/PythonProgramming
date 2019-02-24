import json

a = {"TRTM_ID" : 1000021, "PATIENT_ID" : 1000003,
     "TRTM_TIME" : "2018-09-27 14 : 50 : 28.0",
     "DEVICE_VER_ID" : 3.0000000000, "DEVICE_ID" : "27090062",
     "SCHEMA_VERSION" : 14,
     "TRTM_CYCL" : {"TRTM_CYCLE_ID" : 1000031, "CYCLE_TYPE" : "NIGHTCYCLE", "CYCLE_NUMBER" : "5", "CYCLE_TIME" : "2018-09-27 20 : 24 : 05.0", "TRTM_CYCL_ATTR_ID" : 1000137, "ATTR_CD" : "Cycle", "TYPE_CD" : "CODE"
         , "VALUE_TEXT" : "NULL", "VALUE_INT" : "NULL", "VALUE_TIME" : "NULL", "VALUE_DEC" : "NULL", "VALUE_CD" : "NIGHTCYCLE", "VALUE_FLAG" : "NULL", "VALUE_DOMAIN_CD" : "CycleType", "VALUE_UID" : "NULL"}
     }
with open("testjson.txt","w") as jt:
    jt.write(json.dumps(a))