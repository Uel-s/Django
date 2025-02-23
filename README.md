# Puddle

## Description
Puddle is a Django-based marketplace application designed to facilitate buying and selling of items. It provides users with a seamless experience to browse items, communicate with sellers, and manage their listings.

## Features
- User authentication (Sign up, Login)
- Item listing and management
- Conversation system for buyer-seller communication
- Dashboard for managing your items and conversations
- Search and filter functionality for items
- Responsive design with Tailwind CSS
- Optimized mobile-friendly layouts for all pages
- Consistent image sizing across the application


## Installation Instructions
1. Clone the repository:
   ```bash
   git clone git@github.com:Uel-s/Django.git
   ```
2. Navigate to the project directory:
   ```bash
   cd puddle
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```bash
   python manage.py migrate.
   ```
6. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver.
   ```

## Usage
1. Access the application by navigating to `http://127.0.0.1:8000/` in your web browser.
2. The application is fully responsive and works seamlessly on both mobile and desktop devices.

2. Browse items on the homepage or use the search functionality to find specific items.
3. Sign up or log in to:
   - List new items for sale
   - Start conversations with sellers
   - Manage your items and conversations through the dashboard
4. As an admin, access the admin panel at `http://127.0.0.1:8000/admin/` to manage users, items, and conversations.

## UI/UX Improvements
- Implemented consistent medium-sized images (384x384 pixels) for better visual presentation
- Optimized grid layouts for mobile devices
- Improved image aspect ratio handling and responsiveness

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact Information
For any inquiries, please contact Cartman at redlaert200@gmail.com.
