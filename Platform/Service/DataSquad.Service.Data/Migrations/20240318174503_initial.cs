using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace DataSquad.Service.Data.Migrations
{
    /// <inheritdoc />
    public partial class initial : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "AccessibilityRecords",
                columns: table => new
                {
                    Id = table.Column<long>(type: "bigint", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Latitude = table.Column<float>(type: "real", nullable: false),
                    Longitude = table.Column<float>(type: "real", nullable: false),
                    MeanDepth = table.Column<float>(type: "real", nullable: false),
                    MeanWaveHeight = table.Column<float>(type: "real", nullable: false),
                    MeanInstantAccessProbability = table.Column<float>(type: "real", nullable: false),
                    MeanExpectedDelayHours = table.Column<float>(type: "real", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_AccessibilityRecords", x => x.Id);
                });

            migrationBuilder.CreateIndex(
                name: "IX_AccessibilityRecords_Latitude_Longitude",
                table: "AccessibilityRecords",
                columns: new[] { "Latitude", "Longitude" });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "AccessibilityRecords");
        }
    }
}
