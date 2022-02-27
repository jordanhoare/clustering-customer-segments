USE [customers]
GO

/****** Object:  View [dbo].[Cluster_Output_view]    Script Date: 28/02/2022 9:18:05 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

ALTER view [dbo].[Cluster_Output_view] AS
SELECT * FROM [customers].[dbo].[Cluster_Output]

GO


