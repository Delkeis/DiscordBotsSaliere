using ValorantApi.Models;

namespace ValorantApi.Services;

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
    }

    static bool AddUser(ValorantUser valUser)
    {
        valUser.Id = nextId++;
        ValorantUsers.Add(valUser);
        return true;
    }       
}