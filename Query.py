
class Query:

  def __init__(self,query_id):
      self.query_id = str(query_id)
      self.query_name = 'Query'+str(query_id)
      self.query_txt = 'select * from dual'
      if query_id == 1 :
         self.query_txt = """WITH a AS (
                SELECT ar.name name_artists,
                       al.albumid
                  FROM albums al,
                       artists ar
                 WHERE al.artistid = ar.artistid
                )
                SELECT t.TrackId,
                       t.name track_name,
                       g.Name genre_name,
                       a.name_artists
                  FROM tracks t,
                       genres g,
                       a
                 WHERE t.genreid = g.genreid AND 
                       a.albumid = t.albumid """
      elif query_id ==2 :
            self.query_txt = """
                SELECT c.firstname,
               c.lastname,
               c.address || " " || c.city || " " || CASE COALESCE(c.state, '') 
                                                    WHEN '' THEN "" 
                                                    ELSE c.state || " " END || c.country ||
                                                    CASE COALESCE(c.postalcode, '') 
                                                    WHEN '' THEN "" 
                                                    ELSE  " "||c.postalcode END  full_address,
               c.phone,
               c.email,
               cnt_invoices.cnt
          FROM customers c,
               (
                   SELECT count(1) cnt,
                          customerid
                     FROM invoices
                    GROUP BY customerid
               )
               cnt_invoices
         WHERE c.customerid = cnt_invoices.customerid
                """
      elif query_id ==3 :
            self.query_txt = """select c.country, substr(c.email,instr(c.email,'@')+1) dumain , count(1) from customers c
                    group by c.country, substr(c.email,instr(c.email,'@')+1) """
      elif query_id == 4:
            self.query_txt = """SELECT count(DISTINCT t.albumid),
                   c.country
              FROM invoice_items i,
                   tracks t,
                   invoices inv,
                   customers c
             WHERE i.trackid = t.TrackId AND 
                   i.invoiceid = inv.invoiceid AND 
                   inv.customerid = c.customerid
             GROUP BY c.country;
             """
      elif query_id ==5 :
            self.query_txt ="""WITH a AS (
                SELECT count(DISTINCT t.albumid) cnt,
                       t.albumid,
                       c.country
                  FROM invoice_items i,
                       tracks t,
                       invoices inv,
                       customers c
                 WHERE i.trackid = t.TrackId AND 
                       i.invoiceid = inv.invoiceid AND 
                       inv.customerid = c.customerid
                 GROUP BY t.albumid,
                          c.country
            )
            SELECT a1.albumid,
                   al.title album_name,
                   a1.country,
                   a1.cnt
              FROM a a1,
                   albums al
             WHERE EXISTS (
                       SELECT max_cnt,
                              country
                         FROM (
                                  SELECT max(a.cnt) max_cnt,
                                         a.country
                                    FROM a
                                   GROUP BY a.country
                              )
                              m
                        WHERE m.max_cnt = a1.cnt AND 
                              m.country = a1.country
                   )
            AND 
                   a1.albumid = al.albumid """
      elif query_id ==6 :
            self.query_txt = """WITH a AS (
            SELECT count(DISTINCT t.albumid) cnt,
                   t.albumid,
                   c.country
              FROM invoice_items i,
                   tracks t,
                   invoices inv,
                   customers c
             WHERE i.trackid = t.TrackId AND 
                   i.invoiceid = inv.invoiceid AND 
                   inv.customerid = c.customerid  and 
                   strftime('%Y',inv.invoicedate) >= '2011' and
                   c.country = 'USA'
             GROUP BY t.albumid,
                      c.country
        )
        SELECT a1.albumid,
               al.title album_name,
               a1.country,
               a1.cnt
          FROM a a1,
               albums al
         WHERE EXISTS (
                   SELECT max_cnt,
                          country
                     FROM (
                              SELECT max(a.cnt) max_cnt,
                                     a.country
                                FROM a
                               GROUP BY a.country
                          )
                          m
                    WHERE m.max_cnt = a1.cnt AND 
                          m.country = a1.country
               )
        AND 
               a1.albumid = al.albumid """
      elif query_id ==7 :
            self.query_txt = """SELECT c.customerid,
                   c.firstname,
                   c.lastname
              FROM customers c,
                   invoices i
             WHERE c.customerid = i.customerid
             GROUP BY c.customerid,
                      c.firstname,
                      c.lastname
            HAVING CASE WHEN i.InvoiceDate IS NULL THEN 1 ELSE 0 END +
                   CASE WHEN i.BillingAddress IS NULL THEN 1 ELSE 0 END + 
                   CASE WHEN i.BillingCity IS NULL THEN 1 ELSE 0 END + 
                   CASE WHEN i.BillingState IS NULL THEN 1 ELSE 0 END + 
                   CASE WHEN i.BillingCountry IS NULL THEN 1 ELSE 0 END +
                   CASE WHEN i.BillingPostalCode IS NULL THEN 1 ELSE 0 END + 
                   CASE WHEN i.Total IS NULL THEN 1 ELSE 0 END >= 2 """