Yoy<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">



    <title>Ranking</title>

    <!-- Bootstrap core CSS -->
    <link href="../bootstrap/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="../Static/ranking.css" rel="stylesheet">
  </head>

  <body>



  <!-----Nav bar----->




<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="#">About</a>
  <a href="#">Services</a>
  <a href="#">Clients</a>
  <a href="#">Contact</a>
  <a href="#">Test</a>
  <a href="#">Test</a>
  <a href="#">Test</a>
  <a href="#">Test</a>

</div>
<div id="main">
  <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; Menu</span>
</div>

  <script>
/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.body.style.backgroundColor = "white";
}

</script>



        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
            <h1 class="h1">The amount you spent:</h1>
<div class="dropdown">

              <button class="dropbtn">

                <span data-feather="calendar"></span>

                  Monthly
                <div class="dropdown-content">
                    <li><a href="Weekly">Weekly</a></li>
                    <li> <a href="Monthly">Monthly</a></li>
                    <li><a href="Yearly">Yearly</a></li>
  </div>

              </button>



          </div>

          <canvas class="my-4 w-100" id="myChart" width="900" height="380"></canvas>

          <h2 class="h2">Ranking:</h2>

          <div class="table-responsive">
            <table class="table table-striped table-sm">
              <thead>
                <tr>

                  <th>#</th>
                  <th>Name</th>
                  <th>Avg.Spending</th>
                  <th>Score</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                     <td>1</td>
                    <td>Smith</td>
                    <td>1200</td>
                    <td>10000</td>
                </tr>
                     <tr>
                        <td>2</td>
                        <td>Jackson</td>
                        <td>2000</td>
                         <td>9000</td>
                     </tr>
                 <tr>
                     <td>3</td>
                    <td>Doe</td>
                    <td>2300</td>
                    <td>8500</td>
                </tr>

                </tr>
                     </tbody>
                    </table>
                        </div>
        </main>

                </div>
                  </div>
                        </div>



        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
            <h1 class="h2">Statistics:</h1>

              </div>
              </button>

            </div>
          </div>

        <div><p class="statistics"><b>You spent $1200 on average, you are in the 0.1% percentile!</b></p></div>

        </main>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../bootstrap/jquery-3.3.1.slim.min.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
  crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../bootstrap/jquery-slim.min.js"><\/script>')</script>
    <script src="../bootstrap/popper.min.js"></script>
    <script src="../bootstrap/bootstrap.min.js"></script>

    <!-- Icons -->
    <script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
    <script>
      feather.replace()
    </script>

    <!-- Graphs -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
    <script>
      var ctx = document.getElementById("myChart");
      var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        datasets: [{
            label: 'Average spending',
            data: [1000,2000,3000,4000,5000,6000,7000],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(10, 120, 20, 0.2)',

            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 100, 64, 1)',

            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});

</script>
  </body>
</html>
