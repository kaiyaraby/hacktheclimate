using Microsoft.AspNetCore.Mvc;
using DataSquad.Service.Domain;

namespace DataSquad.Service.API.Controllers;

[ApiController]
[Route("[controller]")]
public class AnalysisController : ControllerBase
{
    private readonly AnalysisModel _analysisModel;

    public AnalysisController(AnalysisModel analysisModel)
    {
        _analysisModel = analysisModel;
    }

    [HttpPost]
    public async Task<IActionResult> Post(List<GeoPoint> region)
    {
        var analysis = await _analysisModel.CreateAccessibilityAnalysis(region);
        return Ok(analysis);
    }
}
