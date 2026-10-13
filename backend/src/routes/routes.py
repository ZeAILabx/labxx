def register_routes(app):
    # Register blueprints
    from src.controllers.auth_controller import auth_bp
    from src.controllers.assessment_controller import assessment_bp
    from src.controllers.profile_controller import profile_bp
    from src.controllers.roadmap_controller import roadmap_bp
    from src.controllers.quests_controller import quests_bp
    from src.controllers.submissions_controller import submissions_bp
    from src.controllers.progress_controller import progress_bp
    from src.controllers.points_controller import points_bp
    from src.controllers.guilds_controller import guilds_bp
    from src.controllers.social_controller import social_bp
    from src.controllers.events_controller import events_bp
    from src.controllers.notifications_controller import notifications_bp
    from src.controllers.achievements_controller import achievements_bp
    from src.controllers.leaderboard_controller import leaderboard_bp
    from src.controllers.admin_controller import admin_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(assessment_bp, url_prefix='/api/assessment')
    app.register_blueprint(profile_bp, url_prefix='/api/profile')
    app.register_blueprint(roadmap_bp, url_prefix='/api/roadmap')
    app.register_blueprint(quests_bp, url_prefix='/api/quests')
    app.register_blueprint(submissions_bp, url_prefix='/api/submissions')
    app.register_blueprint(progress_bp, url_prefix='/api/progress')
    app.register_blueprint(points_bp, url_prefix='/api/points')
    app.register_blueprint(guilds_bp, url_prefix='/api/guilds')
    app.register_blueprint(social_bp, url_prefix='/api/social')
    app.register_blueprint(events_bp, url_prefix='/api/events')
    app.register_blueprint(notifications_bp, url_prefix='/api/notifications')
    app.register_blueprint(achievements_bp, url_prefix='/api/achievements')
    app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')

