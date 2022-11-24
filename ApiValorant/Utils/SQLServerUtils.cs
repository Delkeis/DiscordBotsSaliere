using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.SqlClient;

namespace ValorantApi.Utils{

    class SQLServerUtils{
        public static SqlConnection GetSqlConnection(string datasource, string database, string username, string password)
        {
            string connString = @"Data Source="+datasource+";Initial Catalog="+database+";Persist Security Info=True;User ID="+username+";Password="+password; 
            SqlConnection conn = new SqlConnection(connString);
            return conn;
        }
    }
};