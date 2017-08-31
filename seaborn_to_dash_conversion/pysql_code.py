# get match_id
match_id = 193944

# regular connection
db = pymysql.connect(
    host=host,
    user=user,
    passwd=passwd,
    db=db_name,
    port=port
)
cur = db.cursor(pymysql.cursors.DictCursor)


# get bounce data from Lord's test
cur.execute("""
    select
    h.innings_number as inn,
    h.overs_unique,
    if(b.bowling_type = 'pace', 1, 0) as pace,
    h.release_speed_kph as speed,
    -h.bounce_velocity_ratio_z as bvrz
    from bbb_tracking h
    join bbb_ball b on b.join_key = h.join_key
    where h.match_id = %s
""", match_id)