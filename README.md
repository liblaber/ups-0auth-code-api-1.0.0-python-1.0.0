# Ups0authCode Python SDK 1.0.0

Welcome to the Ups0authCode SDK documentation. This guide will help you get started with integrating and using the Ups0authCode SDK in your project.

## Versions

- API version: `1.0`
- SDK version: `1.0.0`

## About the API

The UPS OAuth Authorization Code API helps integrate UPS services into your business application for providing the service your application grants your customers. For example, you can create UPS shipping labels with shipping rates for merchants from within your application. Since your application will not have access to your customer's UPS login credentials, the OAuth authorization code flow is used to let your customer use their UPS credentials, within your application, in a simple and secure way. Key Business Values: - **Enhanced Transaction Security**: The OAuth Authorization Code flow is more secure and reliable since the access token and the refresh token are never exposed in the browser's URL, thus reducing the risk of leakage or theft. - **Operational Efficiency**: With the ability to obtain a refresh token when the token expires, your application can maintain a long-term and uninterrupted access to the protected resources, without requiring the user to re-authenticate or re-login. Overview of steps in OAuth Authorization Code flow: (1) When user selects Login, the client application redirects to the authorization server's /authorize endpoint. (2) The Authorization Server authenticates the user by asking for their login credentials, and after successful login, the authorization server responds back to the application with an authorization code contained within a redirection URI. (3) The application then sends the authorization code and the redirection URI to the authorization server's /oauth/token endpoint. (4) The authorization server's /token endpoint verifies the authorization code and the application's client ID contained in the redirect URI, and responds with a with an access token, as well as a refresh token. (5) The Client application uses the access token to request information from an UPS API. https://developer.ups.com/api/reference/oauth/authorization-code

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [Basic Authentication](#basic-authentication)
- [Services](#services)
- [Models](#models)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install ups-0auth-auth-code
```

## Authentication

### Basic Authentication

The Ups0authCode API uses Basic Authentication.

You need to provide your username and password when initializing the SDK.

#### Setting the Username and Password

When you initialize the SDK, you can set the username and password as follows:

```py
Ups0authCode(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD"
)
```

If you need to set or update the username and password after initializing the SDK, you can use:

```py
sdk.set_basic_auth("YOUR_USERNAME", "YOUR_PASSWORD")
```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                           |
| :------------------------------------------------------------- |
| [AuthorizeService](documentation/services/AuthorizeService.md) |
| [TokenService](documentation/services/TokenService.md)         |
| [RefreshService](documentation/services/RefreshService.md)     |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                                 | Description |
| :----------------------------------------------------------------------------------- | :---------- |
| [GenerateTokenRequest](documentation/models/GenerateTokenRequest.md)                 |             |
| [GenerateTokenSuccessResponse](documentation/models/GenerateTokenSuccessResponse.md) |             |
| [RefreshTokenRequest](documentation/models/RefreshTokenRequest.md)                   |             |
| [RefreshTokenSuccessResponse](documentation/models/RefreshTokenSuccessResponse.md)   |             |

</details>

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
