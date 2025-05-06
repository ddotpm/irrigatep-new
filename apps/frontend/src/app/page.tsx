export default function Home() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8">IrrigateP Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Projects Card */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Projects</h2>
          <p className="text-gray-600">Manage your irrigation projects</p>
        </div>

        {/* Clients Card */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Clients</h2>
          <p className="text-gray-600">View and manage client information</p>
        </div>

        {/* Equipment Card */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Equipment</h2>
          <p className="text-gray-600">Track equipment and maintenance</p>
        </div>

        {/* Employees Card */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Employees</h2>
          <p className="text-gray-600">Manage your team</p>
        </div>

        {/* Parts Inventory Card */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Parts Inventory</h2>
          <p className="text-gray-600">Track parts and supplies</p>
        </div>

        {/* Invoices Card */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Invoices</h2>
          <p className="text-gray-600">Manage billing and payments</p>
        </div>
      </div>
    </div>
  )
} 