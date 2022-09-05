import os
import logging
import re
from pipeadapter import Fitting
from pipeadapter import OtherFittingError

class concat_fields(Fitting):
    def __init__(this, name="Concat Fields"):
        super().__init__(name)

        this.requiredKWArgs.append("fields")
        this.requiredKWArgs.append("match")

        this.optionalKWArgs["joiner"] = ";"
        this.optionalKWArgs["field_name"] = None

    # Required Fitting method. See that class for details.
    def Run(this):
        if (this.field_name is None):
            this.field_name = f"field_{this.match}"
        
        this.output[this.field_name] = ""
        for field, contents in this.fields.items():
            if (re.search(this.match, field) is not None):
                logging.debug(f"Found match for {this.match} in {field}; will add {contents} to {this.field_name}.")
                if (len(this.output[contents])):
                    this.output[this.field_name] += this.joiner
                this.output[this.field_name] += contents