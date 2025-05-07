from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/team', methods=['GET'])
def team():
    team_info = {
        "company": "Taskly",
        "description": "Taskly is a productivity software platform designed to simplify task management for individuals and teams.",
        "team_members": [
            {
                "name": "Mohit",
                "role": "Technical Lead",
                "bio": "Mohit is a visionary software developer with vast experience in productivity software. He co-founded Taskly with the goal of making task management simple and efficient for everyone."
            },
            {
                "name": "Aditya",
                "role": "Team Lead",
                "bio": "Aditya is a talented developer with a passion for creating intuitive user interfaces. He leads our development team in building robust and user-friendly features for Taskly."
            },
            {
                "name": "Hardik Chawla",
                "role": "Java Lead",
                "bio": "Hardik Chawla is a visionary software developer with vast experience in productivity software. He co-founded Taskly with the goal of making task management simple and efficient for everyone."
            },
            {
                "name": "Ishan",
                "role": "UI/UX Lead",
                "bio": "Ishan brings creativity and user-centered design principles to Taskly. With his innovative approach, he consistently delivers intuitive designs that enhance user experience."
            }
        ]
    }
    return jsonify(team_info)

if __name__ == '__main__':
    app.run(debug=True)
