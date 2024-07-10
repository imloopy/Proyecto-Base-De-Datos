using System;
using System.Data;
using System.Linq;
using System.Collections.Generic;
using Npgsql;

public class PostgreSQLHelper
{
    private string connectionString;

    public PostgreSQLHelper(string connectionString)
    {
        this.connectionString = connectionString;
    }

    public DataTable GetTableData(string tableName, params string[] columns)
    {
        using (NpgsqlConnection connection = new NpgsqlConnection(connectionString))
        {
            connection.Open();

            // Construir la consulta SQL dinámicamente
            string sql = $"SELECT {string.Join(", ", columns)} FROM {tableName}";

            using (NpgsqlCommand command = new NpgsqlCommand(sql, connection))
            {
                using (NpgsqlDataAdapter adapter = new NpgsqlDataAdapter(command))
                {
                    DataTable dataTable = new DataTable();
                    adapter.Fill(dataTable);
                    return dataTable;
                }
            }
        }
    }

    public void AddRelatedColumn(DataTable table, string senderColumnName, string relatedTableName, string destinyColumnName, string relatedColumnName, string savedColumnName)
    {
        // Verificar si la columna especificada existe en la tabla actual
        if (!table.Columns.Contains(senderColumnName))
        {
            throw new ArgumentException($"Column '{senderColumnName}' does not belong to table '{table.TableName}'.");
        }

        // Obtener todos los valores únicos de la columna especificada en la tabla actual
        var uniqueIds = table.AsEnumerable().Select(r => r[senderColumnName]).Distinct().ToList();

        // Verificar si hay valores únicos para evitar consultas innecesarias
        if (uniqueIds.Count == 0)
        {
            return; // No hay valores únicos, no hay nada que buscar
        }

        // Consultar la base de datos para obtener los valores relacionados
        string sql = $"SELECT {destinyColumnName}, {relatedColumnName} FROM {relatedTableName} WHERE {destinyColumnName} IN ({string.Join(",", uniqueIds.Select(id => $"'{id}'"))})";

        using (NpgsqlConnection connection = new NpgsqlConnection(connectionString))
        {
            connection.Open();

            using (NpgsqlCommand command = new NpgsqlCommand(sql, connection))
            {
                using (NpgsqlDataAdapter adapter = new NpgsqlDataAdapter(command))
                {
                    DataTable relatedData = new DataTable();
                    adapter.Fill(relatedData);

                    // Crear un diccionario para mapear los valores de la tabla relacionada
                    var map = relatedData.AsEnumerable()
                                         .ToDictionary(row => row[destinyColumnName], row => row[relatedColumnName]);

                    // Obtener el tipo de datos de la columna relacionada
                    var columnType = relatedData.Columns[relatedColumnName].DataType;

                    // Agregar una nueva columna a la tabla actual y asignar los valores relacionados
                    DataColumn newColumn = new DataColumn(savedColumnName, columnType);
                    table.Columns.Add(newColumn);

                    foreach (DataRow row in table.Rows)
                    {
                        var key = row[senderColumnName];
                        if (map.ContainsKey(key) && map[key] != DBNull.Value)
                        {
                            row[newColumn.ColumnName] = map[key];
                        }
                        else
                        {
                            row[newColumn.ColumnName] = DBNull.Value;
                        }
                    }
                }
            }
        }
    }

    public void RemoveColumn(DataTable table, string columnName)
    {
        if (!table.Columns.Contains(columnName))
        {
            throw new ArgumentException($"Column '{columnName}' does not exist in table '{table.TableName}'.");
        }

        table.Columns.Remove(columnName);
    }

    public void ClearAndInsertTableData(string targetConnectionString, DataTable table, string tableName)
    {
        using (NpgsqlConnection connection = new NpgsqlConnection(targetConnectionString))
        {
            connection.Open();

            using (NpgsqlTransaction transaction = connection.BeginTransaction())
            {
                try
                {
                    // Borrar datos existentes en la tabla de destino
                    string deleteSql = $"DELETE FROM {tableName}";
                    using (NpgsqlCommand deleteCommand = new NpgsqlCommand(deleteSql, connection))
                    {
                        deleteCommand.ExecuteNonQuery();
                    }

                    // Insertar datos de la tabla en la tabla de destino
                    foreach (DataRow row in table.Rows)
                    {
                        string columnNames = string.Join(", ", table.Columns.Cast<DataColumn>().Select(c => c.ColumnName));
                        string columnValues = string.Join(", ", table.Columns.Cast<DataColumn>().Select(c => $"@{c.ColumnName}"));

                        string insertSql = $"INSERT INTO {tableName} ({columnNames}) VALUES ({columnValues})";
                        using (NpgsqlCommand insertCommand = new NpgsqlCommand(insertSql, connection))
                        {
                            foreach (DataColumn column in table.Columns)
                            {
                                insertCommand.Parameters.AddWithValue($"@{column.ColumnName}", row[column.ColumnName]);
                            }
                            insertCommand.ExecuteNonQuery();
                        }
                    }

                    transaction.Commit();
                }
                catch (Exception ex)
                {
                    transaction.Rollback();
                    throw new Exception("Error during data transfer: " + ex.Message);
                }
            }
        }
    }

    public void PrintTable(DataTable table)
    {
        Console.WriteLine($"Tabla: {table.TableName}");

        // Imprimir cada fila de datos
        foreach (DataRow row in table.Rows)
        {
            foreach (var item in row.ItemArray)
            {
                Console.Write($"{item,-20}");
            }
            Console.WriteLine();
        }

        // Imprimir los nombres de las columnas al final
        Console.WriteLine();
        Console.WriteLine("Nombres de las columnas:");
        foreach (DataColumn column in table.Columns)
        {
            Console.Write($"{column.ColumnName,-20}");
        }
        Console.WriteLine();
    }
}

public class Program
{
    public static void Main()
    {
        string connectionString = "Host=localhost;Username=postgres;Password=admin;Database=postgres";
        string targetConnectionString = "Host=localhost;Username=postgres;Password=admin;Database=boletas";

        PostgreSQLHelper db = new PostgreSQLHelper(connectionString);

        string[] requestedColumnsBoleta = { "idBoleta", "idCliente", "idSede", "monto" };
        DataTable tableBoleta = db.GetTableData("Boleta", requestedColumnsBoleta);

        // Agregar la columna relacionada de Cliente
        db.AddRelatedColumn(tableBoleta, "idCliente", "Cliente", "idCliente", "idComuna", "idComunaCliente");
        db.AddRelatedColumn(tableBoleta, "idComunaCliente", "Comuna", "idComuna", "nombreComuna", "ComunaCliente");
        db.AddRelatedColumn(tableBoleta, "idSede", "Sede", "idSede", "idComuna", "idComuna");
        db.AddRelatedColumn(tableBoleta, "idComuna", "Comuna", "idComuna", "nombreComuna", "comunaSede");
        db.RemoveColumn(tableBoleta, "idComunaCliente");

        db.ClearAndInsertTableData(targetConnectionString, tableBoleta, "Boleta");

        // Imprimir la tabla actualizada
        //db.PrintTable(tableBoleta);
       /* 
        targetConnectionString = "Host=localhost;Username=postgres;Password=admin;Database=liquidaciones";
        
        string[] requestedColumnsLiquidacion = { "idLiquidacion", "idEmpleado", "fecha", "monto" };
        DataTable tableLiquidacion = db.GetTableData("Liquidacion", requestedColumnsLiquidacion);
        string[] requestedColumnsLRol = {"idRol", "nombreRol"};
        
        DataTable tableLRol = db.GetTableData("Rol", requestedColumnsLRol);
        db.ClearAndInsertTableData(targetConnectionString, tableLRol, "Rol");
        
        db.AddRelatedColumn(tableLiquidacion, "idEmpleado", "Empleado", "idEmpleado", "idRol", "idRol");
        db.AddRelatedColumn(tableLiquidacion, "idRol", "Rol", "idRol", "nombreRol", "nombreRol");

        //db.PrintTable(tableLiquidacion);
        db.ClearAndInsertTableData(targetConnectionString, tableLiquidacion, "Liquidacion");
        */
    }
}

