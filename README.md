# Voucher_management_system
  # Application Overview
  The Voucher Redemption System is a web-based application that allows administrators to create vouchers with various features such as coupon ID, number of redemptions, and expiry date.   
  Users can then use the coupon ID to redeem vouchers before they expire, choosing between single or multiple redemptions depending on the remaining limit.
  # Application Flow
  # 1) Server Initialization:

    *The application starts by initializing the server using FastAPI.
    *Upon initialization, the server establishes a connection to the database and sets up the necessary routes for handling voucher creation and redemption.
  # 2) Admin Voucher Creation:

    * An administrator accesses the appropriate endpoint to create a new voucher.
    * The administrator provides details such as the coupon ID, number of redemptions, and expiry date.
    * The server receives this information and stores it in the database.
  # 3)User Voucher Redemption:

    *Users who possess a voucher attempt to redeem it before it expires.
    *They access the redemption endpoint with the voucher's ID.
    *The server retrieves the voucher details from the database based on the provided ID.
    *If the voucher is valid and not expired, the server decrements the redemption limit and updates the database accordingly.
    *The server provides feedback to the user, indicating whether the redemption was successful or if the voucher has expired.
  # 4)Multiple Redemptions:

    *In scenarios where users have multiple redemptions available, they can specify the number of redemptions they wish to make.
    *Users provide the voucher ID and the desired number of redemptions to the appropriate endpoint.
    *The server iteratively processes each redemption request, updating the database for each successful redemption.
# 5)Error Handling:

  *Throughout the process, the server performs error handling to manage scenarios such as invalid voucher IDs, expired vouchers, or database connection issues.
  *If an error occurs, the server provides appropriate error messages to users, guiding them on how to proceed or informing them of the issue.
# 6) Database Updates and Persistence:

  *After each voucher creation or redemption, the server ensures that the database is updated accordingly to reflect the latest changes.
  *This ensures data integrity and persistence across server sessions.
# 7)Client Interaction:

  *Users interact with the application primarily through HTTP requests, either directly or via client applications.
  *The server responds to these requests, providing the necessary information or performing the requested actions.
# Requirements
  *Ensure you have the following dependencies installed:
    1)FastAPI: Use pip install fastapi to install FastAPI.
    2)Uvicorn: Install Uvicorn for running the API web app using pip install uvicorn.
    3)Requests: Install Requests to handle requests from the client to the server.
# Running the Application
  To run the API, execute the following command:
    uvicorn server:app --reload
# Architecture
*The project follows a client-server architecture:

  *Server: Handles database operations and routing using FastAPI.
  *Client: Interacts with the server through HTTP requests using the Requests library.
  
# Usage
  1)Start the server by running the provided command.
  2)Access the appropriate endpoints to create vouchers and redeem them based on user requirements.

  
