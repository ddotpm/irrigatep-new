# IrrigateP - Irrigation Project Management System

A comprehensive irrigation project management system with a modern tech stack.

## Project Structure

```
irrigatep/
├── apps/
│   ├── backend/         # FastAPI backend application
│   │   ├── app/        # Main application code
│   │   ├── tests/      # Backend tests
│   │   └── alembic/    # Database migrations
│   └── frontend/       # Next.js frontend application
│       ├── src/        # Source code
│       ├── components/ # Reusable components
│       └── pages/      # Application pages
├── packages/           # Shared packages
├── docker/            # Docker configuration files
└── docs/              # Project documentation
```

## Tech Stack

### Backend
- FastAPI (Python)
- PostgreSQL
- SQLAlchemy
- Alembic
- Docker

### Frontend
- Next.js 14
- TypeScript
- Tailwind CSS
- shadcn/ui
- React Query

## Getting Started

### Prerequisites
- Node.js (v20 or higher)
- Python (v3.11 or higher)
- Docker Desktop
- pnpm (package manager)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pnpm install        # Frontend dependencies
   pip install -r requirements.txt  # Backend dependencies
   ```

3. Start the development environment:
   ```bash
   docker-compose up -d  # Start PostgreSQL
   pnpm dev            # Start frontend
   pnpm backend:dev    # Start backend
   ```

## Development

More detailed documentation can be found in the `/docs` directory. 