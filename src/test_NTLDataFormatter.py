import unittest

from NTLDataFormatter import NTLDataFormatter

class TestNTLDataFormatter(unittest.TestCase):
    def test_getNTLDataObjects(self):
        test_input = {
            "response": {
                "docs": [{
                    "mods.abstract": ["Source: Provided by ITS DataHub (its.dot.gov/data) through the National Transportation Library.",
                        "The Washington site used the reliability guide from Project L02, analysis tools for forecasting reliability and estimating impacts from Project L07, Project L08, and Project C11 as well as the guide on reliability performance measures from the Project L05 product. The Washington site focused on the I-5 and I-405 corridors from Lynnwood to Tukwila (approximately 30 miles long for each corridor running through the Puget Sound metropolitan region), and the SR-522 urban arterial near Seattle. The pilot testing demonstrated that the SHRP 2 Reliability data and analytical products clearly addressed the practical challenges that transportation agencies face when monitoring and analyzing travel time reliability. However, most tools require significant improvements at the application level.",
                        "Project L38D was intended to evaluate a suite of projects to determine their readiness for implementation. Those projects had a logical structure consisting of data collection, analysis, and project prioritization.",
                        "The datasets in this zip file, which is 90.5 MB in size, are in support of SHRP 2 reliability project L38D, \"Pilot testing of SHRP 2 reliability data and analytical products: Washington.\" The project report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3610",
                        "This zip file contains 20 Comma Separated Values (CSV) files, which can be opened using most text editing programs."
                    ],
                    "fgs.state": "Active",
                    "dc.title": ["Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Washington [supporting datasets]",
                        "SHRP 2 reliability project L38D. [supporting datasets]"
                    ],
                    "dc.language": ["English"],
                    "mods.sm_key_words": ["Travel time",
                        "Traffic engineering",
                        "Business practices",
                        "Data analysis",
                        "Data collection",
                        "Pilot studies",
                        "Intelligent transportation systems",
                        "Travel time reliability",
                        "Strategic Highway Research Program 2 (SHRP2)",
                        "SHRP2 Project L38D"
                    ],
                    "fgs.lastModifiedDate": "2019-10-07T17:08:04.927Z",
                    "mods.sm_collection": ["Intelligent Transportation Systems Joint Program Office"],
                    "mods.sm_digital_object_identifier": ["https://doi.org/10.21949/1503765"],
                    "mods.language": ["English"],
                    "mods.ss_publishyear": "2014",
                    "mods.title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Washington [supporting datasets]",
                    "mods.ss_jobid": "821",
                    "rdf.isMemberOf": ["dot:239"],
                    "mods.sm_report_number": ["SHRP 2 reliability project L38D"],
                    "mods.sm_creator": ["Nisbet, John",
                        "Bremmer, Daniela",
                        "Yan, Shuming",
                        "Murshed, Delwar",
                        "Wang, Yinhai",
                        "Zou, Yajie",
                        "Zhu, Wenbo",
                        "Dunlap, Matthew",
                        "Wright, Benjamin",
                        "Zhu, Tao",
                        "Zhang, Yingying"
                    ],
                    "mods.sm_alternate_url": ["https://ntlrepository.blob.core.windows.net/lib/61000/61900/61968/Nisbet_Pilot_Testing_SHRP2_Reliability_Data_Analytical_Prod_Wash_SHRP_2_Rel_Proj_L38D_DATA_2014.zip",
                        "https://ntlrepository.blob.core.windows.net/lib/61000/61900/61968/usdot_itsjpo_shrp2_L38D_20190523.json"
                    ],
                    "mods.sm_corporate_creator": ["Washington (State). Department of Transportation",
                        "University of Washington. Smart Transportation Applications and Research Laboratory",
                        "Second Strategic Highway Research Program (U.S.)"
                    ],
                    "rdf.isOpenAccess": ["true"],
                    "mods.origin": ["2014-01-01; ,"],
                    "dc.description": ["https://doi.org/10.21949/1503765",
                        "2014",
                        "ZIP",
                        "Dataset",
                        "https://ntlrepository.blob.core.windows.net/lib/61000/61900/61968/Nisbet_Pilot_Testing_SHRP2_Reliability_Data_Analytical_Prod_Wash_SHRP_2_Rel_Proj_L38D_DATA_2014.zip",
                        "https://ntlrepository.blob.core.windows.net/lib/61000/61900/61968/usdot_itsjpo_shrp2_L38D_20190523.json",
                        "SHRP 2 reliability project L38D",
                        "Travel time",
                        "Traffic engineering",
                        "Business practices",
                        "Data analysis",
                        "Data collection",
                        "Pilot studies",
                        "Intelligent transportation systems",
                        "Travel time reliability",
                        "Strategic Highway Research Program 2 (SHRP2)",
                        "SHRP2 Project L38D",
                        "United States",
                        "Washington",
                        "United States. National Transportation Library [distributor]",
                        "Nisbet, John",
                        "Bremmer, Daniela",
                        "Yan, Shuming",
                        "Murshed, Delwar",
                        "Wang, Yinhai",
                        "Zou, Yajie",
                        "Zhu, Wenbo",
                        "Dunlap, Matthew",
                        "Wright, Benjamin",
                        "Zhu, Tao",
                        "Zhang, Yingying",
                        "Washington (State). Department of Transportation",
                        "University of Washington. Smart Transportation Applications and Research Laboratory",
                        "Second Strategic Highway Research Program (U.S.)",
                        "National Research Council (U.S.). Transportation Research Board",
                        "United States. Federal Highway Administration",
                        "American Association of State Highway and Transportation Officials",
                        "Intelligent Transportation Systems Joint Program Office",
                        "Source: Provided by ITS DataHub (its.dot.gov/data) through the National Transportation Library.",
                        "The Washington site used the reliability guide from Project L02, analysis tools for forecasting reliability and estimating impacts from Project L07, Project L08, and Project C11 as well as the guide on reliability performance measures from the Project L05 product. The Washington site focused on the I-5 and I-405 corridors from Lynnwood to Tukwila (approximately 30 miles long for each corridor running through the Puget Sound metropolitan region), and the SR-522 urban arterial near Seattle. The pilot testing demonstrated that the SHRP 2 Reliability data and analytical products clearly addressed the practical challenges that transportation agencies face when monitoring and analyzing travel time reliability. However, most tools require significant improvements at the application level.",
                        "Project L38D was intended to evaluate a suite of projects to determine their readiness for implementation. Those projects had a logical structure consisting of data collection, analysis, and project prioritization.",
                        "The datasets in this zip file, which is 90.5 MB in size, are in support of SHRP 2 reliability project L38D, \"Pilot testing of SHRP 2 reliability data and analytical products: Washington.\" The project report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3610",
                        "This zip file contains 20 Comma Separated Values (CSV) files, which can be opened using most text editing programs.",
                        "821"
                    ],
                    "PID": "dot:3616",
                    "mods.raw_date": ["2014-01-01"],
                    "mods.sm_format": ["ZIP"],
                    "mods.sm_corporate_contributor": ["National Research Council (U.S.). Transportation Research Board",
                        "United States. Federal Highway Administration",
                        "American Association of State Highway and Transportation Officials"
                    ],
                    "mods.sm_geographical_coverage": ["United States",
                        "Washington"
                    ],
                    "fgs.createdDate": "2017-08-29T13:16:20.965Z",
                    "mods.alt_title": ["SHRP 2 reliability project L38D. [supporting datasets]"],
                    "mods.sm_resource_type": ["Dataset"],
                    "mods.sm_corporate_publisher": ["United States. National Transportation Library [distributor]"]
                }]
            }
        }
    
        test_NTLDataFormatter = NTLDataFormatter()
        formatted_output = test_NTLDataFormatter.getNTLDataObjects(test_input)

        assert len(formatted_output) == 1
