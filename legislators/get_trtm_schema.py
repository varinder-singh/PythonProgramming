import sys
import pydevd
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *


def main():
    # Invoke pydevd
    pydevd.settrace('169.254.76.0', port=9001, stdoutToServer=True, stderrToServer=True)

    # Create a Glue context
    glueContext = GlueContext(SparkContext.getOrCreate())

    # Create a DynamicFrame using the 'persons_json' table
    persons_DyF = glueContext.create_dynamic_frame.from_catalog(database="legislators", table_name="persons_json")
    """ Adding a new function to be called by Map"""

    def merge_trtm_attr(dynamic_frame_trtm):
        dynamic_frame_trtm["trtm_attr"] = {}
        dynamic_frame_trtm["trtm_attr"]["Street"] = dynamic_frame_trtm["Provider Street Address"]
        dynamic_frame_trtm["trtm_attr"]["City"] = dynamic_frame_trtm["Provider City"]
        dynamic_frame_trtm["trtm_attr"]["State"] = dynamic_frame_trtm["Provider State"]
        dynamic_frame_trtm["trtm_attr"]["Zip.Code"] = dynamic_frame_trtm["Provider Zip Code"]
        dynamic_frame_trtm["trtm_attr"]["Array"] = [dynamic_frame_trtm["Provider Street Address"], dynamic_frame_trtm["Provider City"], dynamic_frame_trtm["Provider State"], dynamic_frame_trtm["Provider Zip Code"]]

        dynamic_frame_trtm["trtm_attr"]["trtm_cycle"] = {}
        dynamic_frame_trtm["trtm_attr"]["trtm_cycle"]["trtm_cycle_attr_id"] = dynamic_frame_trtm["trtm_attr"]["trtm_cycle_attr_id"]

        del dynamic_frame_trtm["Provider Street Address"]
        del dynamic_frame_trtm["Provider City"]
        del dynamic_frame_trtm["Provider State"]
        del dynamic_frame_trtm["Provider Zip Code"]
        return dynamic_frame_trtm
    # Print out information about this data
    print("Count:  ", persons_DyF.count())
    persons_DyF.printSchema()

if __name__ == "__main__":
    main()