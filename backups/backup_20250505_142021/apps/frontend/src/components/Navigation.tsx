import Link from 'next/link'

export function Navigation() {
  return (
    <nav className="bg-white shadow-md">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          <Link href="/" className="text-xl font-bold text-gray-800">
            IrrigateP
          </Link>
          
          <div className="hidden md:flex space-x-4">
            <Link href="/projects" className="text-gray-600 hover:text-gray-900">
              Projects
            </Link>
            <Link href="/clients" className="text-gray-600 hover:text-gray-900">
              Clients
            </Link>
            <Link href="/equipment" className="text-gray-600 hover:text-gray-900">
              Equipment
            </Link>
            <Link href="/employees" className="text-gray-600 hover:text-gray-900">
              Employees
            </Link>
            <Link href="/parts" className="text-gray-600 hover:text-gray-900">
              Parts
            </Link>
            <Link href="/invoices" className="text-gray-600 hover:text-gray-900">
              Invoices
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
} 