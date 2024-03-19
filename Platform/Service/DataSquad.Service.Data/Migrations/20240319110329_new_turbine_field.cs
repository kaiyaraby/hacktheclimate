using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace DataSquad.Service.Data.Migrations
{
    /// <inheritdoc />
    public partial class new_turbine_field : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<float>(
                name: "MeanAnnualExpectedPower",
                table: "TurbineRecords",
                type: "real",
                nullable: false,
                defaultValue: 0f);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "MeanAnnualExpectedPower",
                table: "TurbineRecords");
        }
    }
}
