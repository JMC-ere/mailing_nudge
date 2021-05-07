NUDGE_TYPE = """
select
   nudge_type,
   nudge_name
from
	nudge;
"""
MENU_ID = """
select
   exposure_name,
   menu_id 
from
	exposure;
"""
ES_DLS_01 = """
{
  "size": 0,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "log_day": "%s"
          }
        },
        {
          "term": {
            "page_id": "/voice_text"
          }
        },
        {
          "terms": {
            "action_id": [
              "page_show",
              "focus.voice_text.button",
              "click.voice_text.button"
            ]
          }
        }
      ]
    }
  },
  "aggs": {
    "config": {
      "terms": {
        "field": "action_body.config",
        "size": 1000
      },
      "aggs": {
        "show": {
          "terms": {
            "field": "action_id",
            "size": 1000
          },
          "aggs": {
            "stb": {
              "cardinality": {
                "field": "stb_id"
              }
            }
          }
        },
        "test": {
          "bucket_script": {
            "buckets_path": {
              "show_count": "show['page_show']>_count",
              "click_count": "show['click.voice_text.button']>_count",
              "stb_count": "show['page_show']>stb.value"
            },
            "script": "( params.click_count / params.show_count ) * 100"
          }
        }
      }
    }
  }
}
"""
ES_DLS_02 = """
{
  "size": 0,
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "log_day": "%s"
          }
        },
        {
          "term": {
            "page_id": "/voice_text"
          }
        },
        {
          "terms": {
            "action_id": [
              "page_show",
              "focus.voice_text.button",
              "click.voice_text.button"
            ]
          }
        }
      ]
    }
  },
  "aggs": {
    "target": {
      "terms": {
        "field": "action_body.target",
        "size": 1000
      },
      "aggs": {
        "show": {
          "terms": {
            "field": "action_id",
            "size": 1000
          },
          "aggs": {
            "stb": {
              "cardinality": {
                "field": "stb_id"
              }
            }
          }
        },
        "test": {
          "bucket_script": {
            "buckets_path": {
              "show_count": "show['page_show']>_count",
              "click_count": "show['click.voice_text.button']>_count",
              "stb_count": "show['page_show']>stb.value"
            },
            "script": "( params.click_count / params.show_count ) * 100"
          }
        }
      }
    }
  }
}
"""