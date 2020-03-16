import unittest

from SocrataDataFormatter import SocrataDataFormatter

class TestSocrataDataFormatter(unittest.TestCase):
    def test_getSocrataDataObjects(self):
        test_results = {
            "results": [{
                "resource": {
                    "name": "Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data",
                    "id": "8ect-6jqj",
                    "parent_fxf": None,
                    "description": "Researchers for the Next Generation Simulation (NGSIM)  program collected detailed vehicle trajectory data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, Georgia. Data was collected through a network of synchronized digital video cameras.NGVIDEO, a customized software application developed for the NGSIM program, transcribed the vehicle trajectory data from the video. This vehicle trajectory data provided the precise location of each vehicle within the study area every one-tenth of a second, resulting in detailed lane positions and locations relative to other vehicles. Click the \"Show More\" button below to find additional contextual data and metadata for this dataset.",
                    "attribution": "U.S. Department of Transportation Intelligent Transportation Systems Joint Program Office (JPO) -- Recommended citation: \"U.S. Department of Transportation Federal Highway Administration. (2016). Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data. [Dataset]. Provided by ITS DataHub through Data.transportation.gov. Accessed YYYY-MM-DD from http://doi.org/10.21949/1504477\"",
                    "attribution_link": None,
                    "contact_email": "RDAE_Support@bah.com",
                    "type": "dataset",
                    "updatedAt": "2019-10-29T21:18:37.000Z",
                    "createdAt": "2017-09-01T15:22:44.000Z",
                    "metadata_updated_at": "2019-10-29T21:18:37.000Z",
                    "data_updated_at": "2018-08-27T18:23:53.000Z",
                    "page_views": {
                        "page_views_last_week": 346,
                        "page_views_last_month": 922,
                        "page_views_total": 27706,
                        "page_views_last_week_log": 8.43879185257826,
                        "page_views_last_month_log": 9.850186837645774,
                        "page_views_total_log": 14.757962889739842
                    },
                    "columns_name": [
                        "v_Vel",
                        "Section_ID",
                        "v_Acc",
                        "Global_Y",
                        "v_Class",
                        "Global_Time",
                        "Location",
                        "v_Width",
                        "Lane_ID",
                        "v_length",
                        "D_Zone",
                        "Space_Headway",
                        "Int_ID",
                        "Local_Y",
                        "Time_Headway",
                        "Following",
                        "Movement",
                        "Direction",
                        "Global_X",
                        "Frame_ID",
                        "O_Zone",
                        "Total_Frames",
                        "Vehicle_ID",
                        "Local_X",
                        "Preceding"
                    ],
                    "columns_field_name": [
                        "v_vel",
                        "section_id",
                        "v_acc",
                        "global_y",
                        "v_class",
                        "global_time",
                        "location",
                        "v_width",
                        "lane_id",
                        "v_length",
                        "d_zone",
                        "space_headway",
                        "int_id",
                        "local_y",
                        "time_headway",
                        "following",
                        "movement",
                        "direction",
                        "global_x",
                        "frame_id",
                        "o_zone",
                        "total_frames",
                        "vehicle_id",
                        "local_x",
                        "preceding"
                    ],
                    "columns_datatype": [
                        "Number",
                        "Text",
                        "Number",
                        "Number",
                        "Number",
                        "Number",
                        "Text",
                        "Number",
                        "Number",
                        "Number",
                        "Text",
                        "Number",
                        "Text",
                        "Number",
                        "Number",
                        "Number",
                        "Text",
                        "Text",
                        "Number",
                        "Number",
                        "Text",
                        "Number",
                        "Number",
                        "Number",
                        "Number"
                    ],
                    "columns_description": [
                        "Instantaneous velocity of vehicle in feet/second.",
                        "Section in which the vehicle is traveling. Lankershim Blvd is divided into five\nsections (south of intersection 1; between intersections 1 and 2, 2 and 3, 3 and 4; and north of\nintersection 4). Value of “0” means that the vehicle does not identify with a section of Lankershim\nBoulevard and that the vehicle was in the immediate vicinity of an intersection (Int_ID above).\nPlease refer to the data analysis report for more detailed information",
                        "Instantaneous acceleration of vehicle in feet/second square.",
                        "Y Coordinate of the front center of the vehicle in feet based on CA State\nPlane III in NAD83.",
                        "Vehicle type: 1 - motorcycle, 2 - auto, 3 - truck ",
                        "Elapsed time in milliseconds since Jan 1, 1970.",
                        "Name of street or freeway ",
                        "Width of vehicle in feet",
                        "Current lane position of vehicle. Lane 1 is farthest left lane; lane 5 is farthest\nright lane. Lane 6 is the auxiliary lane between Ventura Boulevard on-ramp and the Cahuenga\nBoulevard off-ramp. Lane 7 is the on-ramp at Ventura Boulevard, and Lane 8 is the off-ramp at\nCahuenga Boulevard.",
                        "Length of vehicle in feet",
                        "Destination zones of the vehicles, i.e., the place where the vehicles exit the\ntracking system. There are 10 destinations in the study area, numbered from 201 through 211.\nOrigin 102 is a one-way off-ramp; hence there is no associated destination number 202. Please\nrefer to the data analysis report for more detailed information.",
                        "Space Headway in feet. Spacing provides the distance between the frontcenter\nof a vehicle to the front-center of the preceding vehicle.",
                        "Intersection in which the vehicle is traveling. Intersections are numbered\nfrom 1 to 4, with intersection 1 at the southernmost, and intersection 4 at the northernmost\nsection of the study area. Value of “0” means that the vehicle was not in the immediate vicinity of\nan intersection and that the vehicle instead identifies with a section of Lankershim Boulevard\n(Section_ID, below). Please refer to the data analysis report for more detailed information.\n",
                        "Longitudinal (Y) coordinate of the front center of the vehicle in feet with\nrespect to the entry edge of the section in the direction of travel.",
                        "Time Headway in seconds. Time Headway provides the time to travel from\nthe front-center of a vehicle (at the speed of the vehicle) to the front-center of the preceding\nvehicle. A headway value of 99",
                        "Vehicle ID of the vehicle following the subject vehicle in the same lane. A\nvalue of '0' represents no following vehicle - occurs at the beginning of the study section and onramp\ndue to the fact that only complete trajectories were recorded by this data collection effort\n(vehicle that did not traverse the downstream boundaries of the section by the end of the study\nperiod were not recorded).",
                        "Movement of the vehicle. 1 - through (TH), 2 - left-turn (LT), 3 - right-turn\n(RT).",
                        " Moving direction of the vehicle. 1 - east-bound (EB), 2 - north-bound (NB), 3 -\nwest-bound (WB), 4 - south-bound (SB).\n",
                        "X Coordinate of the front center of the vehicle in feet based on CA State\nPlane III in NAD83.\nAttribute Domain Val",
                        " Frame Identification number (ascending by start time)",
                        "Origin zones of the vehicles, i.e., the place where the vehicles enter the\ntracking system. There are 11 origins in the study area, numbered from 101 through 111. Please\nrefer to the data analysis report for more detailed information.",
                        " Total number of frames in which the vehicle appears in this data set",
                        "Vehicle identification number (ascending by time of entry into section). REPEATS ARE NOT ASSOCIATED. ",
                        "Lateral (X) coordinate of the front center of the vehicle in feet with respect to\nthe left-most edge of the section in the direction of travel.",
                        "Vehicle ID of the lead vehicle in the same lane. A value of '0' represents no\npreceding vehicle - occurs at the end of the study section and off-ramp due to the fact that only\ncomplete trajectories were recorded by this data collection effort (vehicles already in the section\nat the start of the study period were not recorded)."
                    ],
                    "columns_format": [{
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "true",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "true",
                            "align": "right"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "true",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "true",
                            "align": "right"
                        },
                        {
                            "displayStyle": "plain",
                            "align": "left"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "true",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        },
                        {
                            "precisionStyle": "standard",
                            "noCommas": "false",
                            "align": "right"
                        }
                    ],
                    "download_count": 5042,
                    "provenance": "official",
                    "lens_view_type": "tabular",
                    "blob_mime_type": None,
                    "hide_from_data_json": False,
                    "publication_date": "2018-08-27T15:23:47.000Z"
                },
                "classification": {
                    "categories": ["infrastructure", "public safety"],
                    "tags": [],
                    "domain_category": "Automobiles",
                    "domain_tags": [
                        "freeway",
                        "arterial",
                        "georgia",
                        "atlanta",
                        "california",
                        "emeryville",
                        "los angeles",
                        "peachtree st",
                        "lankershim boulevard",
                        "trajectories",
                        "i-80",
                        "us 101",
                        "next generation simulation (ngsim) vehicle trajectories",
                        "its joint program office (jpo)",
                        "intelligent transportation systems (its)"
                    ],
                    "domain_metadata": [{
                            "key": "Common-Core_Contact-Email",
                            "value": "james.colyar@dot.gov"
                        },
                        {
                            "key": "Common-Core_Last-Update",
                            "value": "2016"
                        },
                        {
                            "key": "Common-Core_License",
                            "value": "https://creativecommons.org/licenses/by-sa/4.0/"
                        },
                        {
                            "key": "Common-Core_Program-Code",
                            "value": "021:013"
                        },
                        {
                            "key": "Common-Core_Public-Access-Level",
                            "value": "public"
                        },
                        {
                            "key": "Common-Core_Temporal-Applicability",
                            "value": "2005-04-20/2006-11-09"
                        },
                        {
                            "key": "Common-Core_Is-Quality-Data",
                            "value": "True"
                        },
                        {
                            "key": "Common-Core_Language",
                            "value": "English"
                        },
                        {
                            "key": "Common-Core_Geographic-Coverage",
                            "value": "Los Angeles, California; Emeryville, California; Atlanta, Georgia"
                        },
                        {
                            "key": "Common-Core_Publisher",
                            "value": "USDOT"
                        },
                        {
                            "key": "Common-Core_Update-Frequency",
                            "value": "R/PT0.1S"
                        },
                        {
                            "key": "Common-Core_Bureau-Code",
                            "value": "021:00"
                        },
                        {
                            "key": "Common-Core_Contact-Name",
                            "value": "James Colyar"
                        }
                    ]
                },
                "metadata": {
                    "domain": "data.transportation.gov",
                    "license": "Creative Commons Attribution | Share Alike 3.0 Unported"
                },
                "permalink": "https://data.transportation.gov/d/8ect-6jqj",
                "link": "https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj",
                "owner": {
                    "id": "khmm-n2z7",
                    "display_name": "Julia Lien"
                }
            }]
        }
        
        test_socrata_data_formatter = SocrataDataFormatter()
        formatted_results = test_socrata_data_formatter.getSocrataDataObjects(test_results, "dtg")

        assert len(formatted_results) == 1
        assert formatted_results[0].dh_source_name == "dtg"