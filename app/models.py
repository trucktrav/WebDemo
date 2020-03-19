from app import db
# from assets import Asset
# from units import Unit


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Assets(db.Model):
    __tablename__ = 'Assets'
    id = db.Column(db.Integer, primary_key=True)
    # Update on creation ############################
    asset_type = db.Column(db.String(64))
    medium = db.Column(db.String(64))
    asset_num = db.Column(db.Integer)
    poe = db.Column(db.String(64))

    # Load from CSV ##################################
    max_weight = db.Column(db.Float)
    max_people = db.Column(db.Float)
    speed = db.Column(db.Float)
    refuel_time = db.Column(db.Float)
    load_time = db.Column(db.Float)
    unload_time = db.Column(db.Float)
    max_range = db.Column(db.Float)
    max_fly_time = db.Column(db.Float)
    rest_time = db.Column(db.Float)

    # Attributes that will be updated ###################
    # capacities___________________________________________________________
    available_weight = db.Column(db.Integer)
    available_people = db.Column(db.Integer)
    transported_weight = db.Column(db.Integer)
    transported_people = db.Column(db.Integer)
    current_unload_day = db.Column(db.Integer)

    temp_transported_weight = db.Column(db.Integer)
    temp_transported_people = db.Column(db.Integer)
    # availability_________________________________________________________
    isFree = db.Column(db.Boolean)
    # time_________________________________________________________________
    fly_time = db.Column(db.Integer)
    refuel_delay = db.Column(db.Integer)
    rest_delay = db.Column(db.Integer)
    throughput_holding_delay = db.Column(db.Integer)
    poe_to_pod_time = db.Column(db.Integer)
    unload_start_time = db.Column(db.Integer)
    unload_end_time = db.Column(db.Integer)
    old_unload_start_time = db.Column(db.Integer)
    unload_start_time_days = db.Column(db.Integer)
    asset_total_time = db.Column(db.Integer)
    intended_weight = db.Column(db.Integer)
    weight_moved = db.Column(db.Boolean)
    new_pod_arrival_time = db.Column(db.Integer)
    # locations and distances______________________________________________
    fly_distance = db.Column(db.Integer)
    pod = db.Column(db.String(64))
    #        eligible_poes = []
    # units________________________________________________________________
    unit_nums_to_deploy = db.Column(db.String(64))

    def __init__(self, row):
        for f in row._fields:
            self.__dict__[f] = row.__getattribute__(f)

    def p_html(self):
        ret = ""
        for k, v in self.__dict__.items():
            ret += "test"
            # ret += '<li><span class ="caret" > {} < / span >'.format(k)
            # ret += '<ul class="nested"><li>{}</li></ul></li>'.format(v)

        return ret

# class Units(db.Model):
#     __tablename__ = 'Units'
#     id = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String)
#     Service = db.Column(db.String)
#     Cargo = db.Column(db.Integer)
