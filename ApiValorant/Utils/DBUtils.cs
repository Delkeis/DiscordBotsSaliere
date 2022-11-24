using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;


namespace ValorantApi.Utils
{
    class DBUtils{
        public static SqlConnection GetDbConnection(){
            string datasource = @"LOCALHOST";
            string database = "ValorantData";
            string username = @"ALTECA\jmbernard";
            string password = "motdepass";
            return SQLServerUtils.GetSqlConnection(datasource, database, username, password);
        }
    }
}