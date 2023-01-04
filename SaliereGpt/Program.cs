using Discord;
using Discord.WebSocket;
using Microsoft.Extensions.Configuration;
using OpenAI_API;
using System;
using System.Threading.Tasks;

internal class Program
{
    private IConfigurationRoot? _config;
    private DiscordSocketClient _client;

    static async Task Main(string[] args)
    {
        OpenAIAPI api = new OpenAIAPI();

        await new Program().InitBot(args);
    }
    async Task InitBot(string[] args)
    {
        try
        {
            Console.WriteLine("[info] Loading config file..");
            _config = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("config.json", optional: false, reloadOnChange: true)
                .Build();
            _client = new DiscordSocketClient();

            await _client.LoginAsync(TokenType.Bot, _config.GetValue<string>("discord:token"));
            Console.WriteLine("Bot is ready !");
        }
        catch(Exception ex)
        {
            // This will catch any exceptions that occur during the operation/setup of your bot.

            // Feel free to replace this with what ever logging solution you'd like to use.
            // I may do a guide later on the basic logger I implemented in my most recent bot.
            Console.Error.WriteLine(ex.ToString());
        }
    }

     async Task RunAsync(string[] args)
    {
        return;
    }
}