#
# Config Class for the requirements for rmtoo
#

class Config:
    # development - team at flonatel
    # users - users from the Internet (sourceforge replies and wishes)
    # customers - people and companies who are flonatel's customers
    stakeholders = ["development", "management", "users", "customers"]
    inventors = ["flonatel", ]

    reqs_spec = \
        {
           "directory": "doc/requirements",
           "commit_interval": 
           # This is used for all-day work:
           ["FILES", "FILES"],
           # This is used for releases (epoch -> HEAD)
           #["7018a441475fb5837be18725a4b40e8d9ef100b1", "HEAD"],
           "default_language": "en_GB",
           "dependency_notation": set(["Solved by", ])
        }

    topic_specs = \
        {
          "ts_common": ["doc/topics", "ReqsDocument"],
        }

    analytics_specs = \
        { 
           "stop_on_errors": False,
           "topics": "ts_common",
        }

    output_specs = \
        [ 
          ["prios", 
           ["ts_common", "artifacts/reqsprios.tex"]],

          ["graph",
           ["ts_common", "artifacts/req-graph1.dot"]],

          ["graph2",
           ["ts_common", "artifacts/req-graph2.dot"]],

          ["stats_reqs_cnt", 
           ["ts_common", "artifacts/stats_reqs_cnt.csv"]],

          ["latex2", 
           ["ts_common", "artifacts//reqtopics.tex"]],

          ["html", 
           ["ts_common", 
            "artifacts/html", "doc/html/header.html",
            "doc/html/footer.html"]],

          ["version1",
           ["ts_common", "artifacts/reqs-version.txt"]],

          ["oopricing1",
           ["ts_common", "artifacts/reqspricing"]],

          ["tlp1",
           ["ts_common", "artifacts/reqdeps1.tlp"]],
        ]

    output_specs2 = \
        [
          ["tlp1",
           ["ts_common", "artifacts/reqdeps1.tlp"]],
        ]
