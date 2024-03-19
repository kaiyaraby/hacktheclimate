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
    [Route("accessibilityAnalysis")]
    public async Task<IActionResult> PostAccessibilityAnalysis(List<GeoPoint> region)
    {
        var analysis = await _analysisModel.CreateAccessibilityAnalysis(region);
        return Ok(analysis);
    }

    [HttpPost]
    [Route("turbineAnalysis")]
    public async Task<IActionResult> PostTurbineAnalysis(List<GeoPoint> region)
    {
        var analysis = await _analysisModel.CreateTurbineAnalysis(region);
        return Ok(analysis);
    }
}
