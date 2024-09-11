-- Drop healthpal database if it exists
DROP DATABASE IF EXISTS `healthpal`;

-- Create the healthpal database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `healthpal`;

USE healthpal;

CREATE TABLE user (
    user_id INT NOT NULL,
    name VARCHAR(40) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(40) NOT NULL,
    height FLOAT(3) NOT NULL,
    weight FLOAT(5) NOT NULL,
    contact_details VARCHAR(40) NOT NULL,
    nationality VARCHAR(40) NOT NULL,
    email VARCHAR(40) NOT NULL,
    location_group VARCHAR(40) NOT NULL,
    school VARCHAR(80) NOT NULL,
    password VARCHAR(40) NOT NULL,
    parent_id INT NULL,
    role VARCHAR(40) NOT NULL,
    created_date DATETIME NOT NULL,
    last_login DATETIME NOT NULL,
    total_point INT NOT NULL,
    health_tier INT NOT NULL,
    workout_frequency INT NOT NULL,
    preferred_intensity INT NOT NULL,
    goal_date DATE NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE events (
    event_id INT NOT NULL,
    title VARCHAR(40) NOT NULL,
    second_title TEXT NOT NULL,
    description TEXT NOT NULL,
    location VARCHAR(40) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    organiser VARCHAR(40) NOT NULL,
    event_type VARCHAR(40) NOT NULL,
    created_date DATETIME NOT NULL,
    max_signups INT NOT NULL,
    current_signups INT NOT NULL,
    mode VARCHAR(40) NOT NULL,
    participant_remark VARCHAR(200) NOT NULL,
    entry_code VARCHAR(40) NULL,
    event_point INT NOT NULL,
    event_program VARCHAR(200) NOT NULL,
    tier INT NOT NULL,
    organiser_phone VARCHAR(15) NOT NULL,
    organiser_email VARCHAR(200) NOT NULL,
    PRIMARY KEY (event_id)
);

CREATE TABLE user_events (
    user_event_id INT NOT NULL,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    registered BOOLEAN NOT NULL,
    completed BOOLEAN NOT NULL,
    PRIMARY KEY (user_event_id),
    FOREIGN KEY (user_id) REFERENCES user (user_id),
    FOREIGN KEY (event_id) REFERENCES events (event_id)
);

CREATE TABLE cards (
    card_id INT NOT NULL,
    title VARCHAR(40) NOT NULL,
    card_type VARCHAR(40) NOT NULL,
    points_required INT NOT NULL,
    event_id INT NULL,
    description VARCHAR(200) NOT NULL,
    recommendation varchar(300) NOT NULL,
    PRIMARY KEY (card_id),
    FOREIGN KEY (event_id) REFERENCES events (event_id)
);

CREATE TABLE user_cards (
    user_card_id INT NOT NULL,
    user_id INT NOT NULL,
    card_id INT NOT NULL,
    earned_date DATETIME NOT NULL,
    PRIMARY KEY (user_card_id),
    FOREIGN KEY (user_id) REFERENCES user (user_id),
    FOREIGN KEY (card_id) REFERENCES cards (card_id)
);

CREATE TABLE health (
    health_data_id INT NOT NULL,
    user_id INT NOT NULL,
    recorded_date DATE NOT NULL,
    calories INT NOT NULL,
    steps INT NOT NULL,
    sleep_hours FLOAT NOT NULL,
    mvpa_minutes INT NOT NULL,
    calories_per_meal INT NOT NULL,
    PRIMARY KEY (health_data_id),
    FOREIGN KEY (user_id) REFERENCES user (user_id)
);

CREATE TABLE health_recommendation (
    recommendation_id INT NOT NULL,
    user_id INT NOT NULL,
    health_goal VARCHAR(40) NOT NULL,
    recommendation_text TEXT NOT NULL,
    generated_date DATETIME NOT NULL,
    progress VARCHAR(40) NOT NULL,
    PRIMARY KEY (recommendation_id),
    FOREIGN KEY (user_id) REFERENCES user (user_id)
);

CREATE TABLE health_coin (
    points_id INT NOT NULL,
    user_id INT NOT NULL,
    points_earned INT NOT NULL,
    earned_date DATETIME NOT NULL,
    source VARCHAR(40) NOT NULL,
    PRIMARY KEY (points_id),
    FOREIGN KEY (user_id) REFERENCES user (user_id)
);

CREATE TABLE performance (
    record_id VARCHAR(40) NOT NULL,
    user_id INT NOT NULL,
    date DATETIME NOT NULL,
    remark TEXT NOT NULL,
    PRIMARY KEY (record_id),
    FOREIGN KEY (user_id) REFERENCES user (user_id)
);

