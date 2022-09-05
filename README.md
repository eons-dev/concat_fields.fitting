# Concatenate Fields Fitting

Combine multiple fields through [Pipeadapter](https://github.com/infrastructure-tech/lib_pipeadapter)

## Inputs

### Required
* `fields` - a dictionary of fields and their contents
* `match` - the regex to match

### Optional
* `joiner` (';') - added between matches
* `field_name` (field_`match`) - what to call the output