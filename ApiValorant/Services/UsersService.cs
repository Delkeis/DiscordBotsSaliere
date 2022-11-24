using ValorantApi.Models;

namespace ValorantApi.Services;

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;

public class UsersService{
    static List<ValorantUser> ValorantUsers { get; }
    static int nextId = 2;
    static UsersService()
    {
        ValorantUsers = new List<ValorantUser>
        {
            new ValorantUser { Id = 1, Name = "john doe"},
            new ValorantUser { Id = 2, Name = "jannet doe"}
        };
        Console.WriteLine("Connection to database");
        SqlConnection conex  = Utils.DBUtils.GetDbConnection();
        try{
            Console.WriteLine("Connection to database");
            conex.Open();
            Console.WriteLine("Connect Succcesss");
        }
        catch (Exception e)
        {
            Console.WriteLine("Error : {0}", e.Message);
        }
    }

    static bool AddUser(ValorantUser valUser)
    {
        valUser.Id = nextId++;
        ValorantUsers.Add(valUser);
        return true;
    }       
}