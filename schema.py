table_person = '''
    CREATE TABLE IF NOT EXISTS MAIN.ADA.PERSON (
        PERSON_ID NUMBER(38,0) NOT NULL,
        HOUSEHOLD_ID NUMBER(38,0),
        AGE VARCHAR(50),
        GENDER VARCHAR(50),
        EDUCATION_LEVEL VARCHAR(100),
        AREA_OF_OCCUPATION VARCHAR(100),
        HAS_DRIVER_LICENSE VARCHAR(50),
        IS_DISABLED VARCHAR(100),
        SECTOR_IF_PRIVATE_WORKER VARCHAR(100),
        SECTOR_IF_CIVIL_SERVANT VARCHAR(100),
        EXPF_PERSON FLOAT,
        primary key (PERSON_ID)
    );
'''

table_household = '''
    CREATE TABLE IF NOT EXISTS MAIN.ADA.HOUSEHOLD (
        household_id             NUMBER,
        people_in_household      NUMBER,
        bathrooms                NUMBER,
        bedrooms                 NUMBER,
        vehicles                 NUMBER,
        bicycles                 NUMBER,
        motorcycles              NUMBER,
        dwelling_type            STRING,
        income                   STRING,
        household_tenure         STRING,
        piped_water_supply       STRING,
        street_pavement          STRING,
        private_parking_space    STRING,
        year_of_newest_vehicle   STRING,
        domestic_worker          STRING,
        cable_tv                 STRING,
        social_assistence        STRING,
        expf_household           FLOAT,
        macrozone                NUMBER,
        administrative_region    STRING
    );
'''

table_stage = '''
    CREATE TABLE IF NOT EXISTS MAIN.ADA.STAGE (
        stage_id             INT,
        household_id         INT,
        person_id            INT,
        trip_id              INT,
        mode                STRING,
        payment             STRING,
        parking_type        STRING,
        bus_route           STRING,
        boarding_station    STRING,
        arrival_station     STRING,
        stage_cost          STRING
    );
'''

table_trip = '''
    CREATE TABLE IF NOT EXISTS MAIN.ADA.TRIP (
        trip_id                                  INT,
        household_id                             INT,
        person_id                                INT,
        tz_origin                                INT,
        tz_destination                           INT,
        ar_origin                                STRING,
        ar_destination                           STRING,
        mode_category                             STRING,
        mode_type                                 STRING,
        activity_origin                           STRING,
        activity_destination                      STRING,
        activity_origin_companion                 STRING,
        activity_destination_companion            STRING,
        trip_activity                             STRING,
        trip_activity_category                    STRING,
        trip_activity_consolidated                STRING,
        trip_activity_consolidated_category       STRING,
        origin_time                               STRING,
        destination_time                          STRING,
        trip_less_than_500m                        INT,
        trip_duration                             STRING,
        includes_walk                              INT,
        includes_bicycle                           INT,
        includes_subway                            INT,
        includes_brt                               INT,
        includes_bus                               INT,
        includes_unlicensed_service                INT,
        includes_private_charter                   INT,
        includes_school_bus                        INT,
        includes_car_as_driver                     INT,
        includes_car_as_passenger                  INT,
        includes_motorcycle_as_driver              INT,
        includes_motorcycle_as_passenger           INT,
        includes_taxi                              INT,
        includes_motorbicycle_taxi                 INT,
        includes_private_driver                    INT,
        includes_other_modes                       INT,
        includes_active_transportation             INT,
        includes_individual_transportation         INT,
        includes_collective_transportation         INT,
        active_transport_walk                      INT,
        active_transport_bicycle                   INT,
        collective_public_transport                INT,
        collective_private_transport               INT,
        individual_private_transport              INT,
        individual_public_transport               INT,
        other_modes                                INT,
        expf_trip                                  FLOAT,
        expf_trip_adjusted                         FLOAT
    );
'''