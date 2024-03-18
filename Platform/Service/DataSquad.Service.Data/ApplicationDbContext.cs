using Microsoft.EntityFrameworkCore;

namespace DataSquad.Service.Data;

public partial class ApplicationDbContext : DbContext
{

    public DbSet<AccessibilityRecordEntity> AccessibilityRecords { get; set; }

    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        OnModelCreatingPartial(modelBuilder);
        AccessibilityRecordEntity.OnModelCreating(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
