def migrate_record(schema, record):
    new_record = {}
    
    # In the record check if it matches anything in 
    for kr, vr in record.items():
        for ks, vs in schema.items():
            new_record.setdefault(ks, vs)
        new_record[kr] = vr
        
    return new_record