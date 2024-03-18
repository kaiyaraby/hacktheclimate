using DataSquad.Service.API;
using DataSquad.Service.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
Console.WriteLine(connectionString);
// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddControllers();
builder.Services.AddDbContext<ApplicationDbContext>(
        options => options.UseSqlServer(connectionString));
builder.Services.AddTransient<AnalysisModel>();

var allowSpecificOrigins = "_allowSpecificOrigins";

builder.Services.AddCors(options =>
{
options.AddPolicy(name: allowSpecificOrigins,
        policy  =>
        {
        policy.WithOrigins("http://localhost:3000");
        });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();

}

app.UseHttpsRedirection();

app.MapControllers();

app.UseCors(allowSpecificOrigins);

app.Run();
