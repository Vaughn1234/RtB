filter_query = """
    query ($code: String! $start: Float! $end: Float!){
      

      
        reportData {
            report(code: $code){ 
                events(
                    startTime: $start, 
                    endTime: $end, 
                    filterExpression: "type = \\"cast\\" and ability.id = 315508 or type =\\"applybuff\\" and ability.id = 193358 or type =\\"applybuff\\" and ability.id = 193356 or type =\\"applybuff\\" and ability.id = 193357 or type =\\"applybuff\\" and ability.id = 199600 or type =\\"applybuff\\" and ability.id = 199603 or type =\\"applybuff\\" and ability.id = 193359"
)
       {
                    data
      }
    }
  }
  }
  

"""

filter_query_two = """query 
EventData
 
 {
  reportData {
    report(code: "gxKFf9HvTPYnzJCc") {
      events(
        startTime: 33037
        endTime: 622697
        filterExpression: "type = \\"cast\\" and ability.id = 315508 or type =\\"applybuff\\" and ability.id = 193358 or type =\\"applybuff\\" and ability.id = 193356 or type =\\"applybuff\\" and ability.id = 193357 or type =\\"applybuff\\" and ability.id = 199600 or type =\\"applybuff\\" and ability.id = 199603 or type =\\"applybuff\\" and ability.id = 193359"
)
       {
        data
        nextPageTimestamp
      }
    }
  }
}"""


get_start_and_end = """
query ($code: String!){ 
  reportData {
    report(code: $code)
      {fights( killType: Kills)
        {
          startTime 
          endTime 
        }
      }
}
}"""

get_report_ids = """query worldData {
  worldData {
    encounter(id:2417) {
      characterRankings (className:\"Rogue\", specName:\"Outlaw\",page: 3,serverRegion:\"EU\"
     )
      
    }
  }
}"""