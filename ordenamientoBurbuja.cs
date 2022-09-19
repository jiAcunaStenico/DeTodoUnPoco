class Program
{
    static void Main(string[] args)
    {
        int[] vector = new int[5];
        int aux;
        for (int i = 0; i < 5; i++)
        {
            Console.Write("Valor "+ (i+1) +" :");
            vector[i] = Convert.ToInt32(Console.ReadLine());
        }
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                if (vector[j] > vector[j+1])
                {
                    aux = vector[j];
                    vector[j] = vector[j + 1];
                    vector[j + 1] = aux;
                }
            }
        }
        Console.Write("Lista Ordenada:\n");
        for (int i = 0; i < 5; i++)
        {                
            Console.Write(vector[i] +"\n");
        }
        Console.Read();
    }
}