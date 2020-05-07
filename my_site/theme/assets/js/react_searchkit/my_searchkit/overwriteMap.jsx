import {default as ResultsListItem} from './ResultsListItem'
import {default as searchConfig} from './configRSK'

function overwriteMap () {

    return {
        config: searchConfig(),
        templates:{
            resultsItem:  ResultsListItem
        }
        }
}
export default overwriteMap;
