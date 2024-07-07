using System;
using System.Collections.Generic;
using Npgsql;

class Program
{
    static void Main(string[] args)
    {
        // Connection string to connect to your PostgreSQL database
        string connectionString = "Host=localhost;Username=postgres;Password=admin;Database=postgres";

        // Create a connection to the PostgreSQL database
        using (var connection = new NpgsqlConnection(connectionString))
        {
            connection.Open();

            // SQL query to get all table names
            string sqlTables = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'";

            Dictionary<string, List<Entidad>> diccionarioEntidades = new Dictionary<string, List<Entidad>>();

            using (var cmdTables = new NpgsqlCommand(sqlTables, connection))
            using (var readerTables = cmdTables.ExecuteReader())
            {
                while (readerTables.Read())
                {
                    string tableName = readerTables.GetString(0);
                    Entidad entidad = new Entidad(tableName);

                    // Query to get column names and types for the current table
                    string sqlColumns = $"SELECT column_name FROM information_schema.columns WHERE table_name = '{tableName}'";


		    Console.WriteLine(sqlColumns);
		    /*
                    // Create a new command for columns query
                    using (var cmdColumns = new NpgsqlCommand(sqlColumns, connection))
                    using (var readerColumns = cmdColumns.ExecuteReader())
                    {
                        while (readerColumns.Read())
                        {
                            string columnName = readerColumns.GetString(0);
                            entidad.Valores[columnName] = null; // Initialize with null or default value
                        }
                    }*/

                    // Add entidad to dictionary
                    diccionarioEntidades[tableName] = new List<Entidad> { entidad };
                }
            }

            // Display the results
            foreach (var kvp in diccionarioEntidades)
            {
                Console.WriteLine($"Tabla: {kvp.Key}");
                foreach (var entidad in kvp.Value)
                {
                    entidad.MostrarValores();
                }
            }
        }
    }
}

