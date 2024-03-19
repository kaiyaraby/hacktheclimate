using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace DataSquad.Service.Data.Migrations
{
    /// <inheritdoc />
    public partial class add_turbine_analysis : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "TurbineRecords",
                columns: table => new
                {
                    Id = table.Column<long>(type: "bigint", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Latitude = table.Column<float>(type: "real", nullable: false),
                    Longitude = table.Column<float>(type: "real", nullable: false),
                    MeanAvailability = table.Column<float>(type: "real", nullable: false),
                    MeanCostPerKiloWatt = table.Column<float>(type: "real", nullable: false),
                    MeanDowntime = table.Column<float>(type: "real", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_TurbineRecords", x => x.Id);
                });

            migrationBuilder.CreateIndex(
                name: "IX_TurbineRecords_Latitude_Longitude",
                table: "TurbineRecords",
                columns: new[] { "Latitude", "Longitude" });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "TurbineRecords");
        }
    }
}
