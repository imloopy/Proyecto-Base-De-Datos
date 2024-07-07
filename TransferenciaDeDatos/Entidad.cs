using System;
using System.Collections.Generic;

public class Entidad {
    public string NombreEntidad { get; set; }
    public List<object> Atributos { get; set; }
    public Dictionary<string, object> Valores { get; set; }

    public Entidad(string nombreEntidad) {
        NombreEntidad = nombreEntidad;
        Atributos = new List<object>();
        Valores = new Dictionary<string, object>();
    }

    public void AgregarAtributo(object atributo) {
        if (atributo is string || atributo is int || atributo is float) {
            Atributos.Add(atributo);
        } else {
            throw new ArgumentException("El atributo debe ser de tipo string, int o float.");
        }
    }

    public void MostrarAtributos() {
        Console.WriteLine($"Nombre de la Entidad: {NombreEntidad}");
        Console.WriteLine("Atributos:");
        foreach (var atributo in Atributos) {
            Console.WriteLine(atributo);
        }
    }

    public void AgregarValor(string atributo, object valor) {
        Valores[atributo] = valor;
    }

    public void MostrarValores() {
        Console.WriteLine($"Valores de la Entidad: {NombreEntidad}");
        foreach (var kvp in Valores) {
            Console.WriteLine($"{kvp.Key}: {kvp.Value}");
        }
    }
}

