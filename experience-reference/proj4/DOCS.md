# Project Instructions: NotesApp

This document provides architectural guidance, conventions, and workflows for the NotesApp project.

## Architecture Overview

The project follows a feature-based folder structure within `src/app/features`. Each feature is self-contained, including its components, services, and styles.

### Core Tiers
- **Core (`src/app/core`):** Global services and singleton logic (e.g., `GlobalService` for window resizing).
- **Features (`src/app/features`):** Business logic and UI components organized by feature (e.g., `editor`, `search`, `items-container`).
- **Shared (`src/app/shared`):** Common models, utilities, and components used across multiple features.

## Technical Standards

### State Management
- **Angular Signals:** Use Signals for both local and global state management. Prefer `signal` and `computed` over manual change detection.
- **RxJS:** Primarily used for asynchronous operations and data streams (e.g., `ItemsSyncService.getItems()`).

### Data Handling
- **Mock Database:** The application currently uses a `dummyDatabase` (defined in `src/app/shared/models/item.model.ts`) to simulate backend CRUD operations. 
- **Sync Services:** Features should use dedicated sync services (e.g., `ItemsSyncService`) to coordinate data updates across the application.

## Conventions & Style
- **Naming:** Follow standard Angular naming conventions (e.g., `feature-name.component.ts`, `feature-name.service.ts`).
- **Styles:** Use SCSS for styling. Prefer component-specific styles over global styles when possible.
- **Components:** Components should be `standalone: true` as per Angular 18 defaults.

## Key Features
- **Editor:** Handles note creation and editing logic.
- **Items Container:** Manages the list of notes and synchronization.
- **Search:** Implements client-side filtering logic.
- **Resize:** Handles responsive design adjustments dynamically.
