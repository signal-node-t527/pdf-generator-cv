# NotesApp

A modern, responsive note-taking application built with Angular 18. This app provides a seamless CRUD experience with reactive elements and a focus on usability.

## 🚀 Features

- **CRUD Operations:** Create, Read, Update, and Delete notes.
- **Real-time Search:** Filter notes by title or content instantly.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Selection Mode:** Batch delete notes with an intuitive selection interface.
- **Interactive Editor:** A dedicated space for crafting and refining your notes.

## 🛠️ Tech Stack

- **Framework:** [Angular 18](https://angular.dev/)
- **State Management:** Angular Signals
- **Asynchronous Logic:** RxJS
- **Styling:** SCSS / Angular Material (CDK)
- **Data Simulation:** Custom mock database for demo purposes.

## 🏗️ Architecture

The project is organized into feature-based modules to ensure maintainability and scalability:

- `src/app/features/`: Contains feature-specific components and services (Editor, Search, Item List, etc.).
- `src/app/core/`: Global services and application-wide configurations.
- `src/app/shared/`: Reusable models and utilities.

## 🏁 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v18 or higher)
- [Angular CLI](https://angular.dev/tools/cli)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd notes-app
   ```
3. Install dependencies:
   ```bash
   npm install
   ```

### Development Server

Run `npm start` (or `ng serve`) for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## 🧪 Testing

Run `npm test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## 📄 License

This project is licensed under the MIT License.
