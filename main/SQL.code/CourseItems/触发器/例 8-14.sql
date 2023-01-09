Begin
DECLARE @payment decimal(10,2),@balance money,@State char(1)
SET @payment=(Select payamount From inserted)
SET @balance=(Select Balance from Table_Card Where Table_Card.CardID = (Select CardID From inserted))
SET @State=(Select State from Table_Card Where Table_Card.CardID = (Select CardID From inserted))
IF @payment<@balance AND @State=0
	begin
	UPDATE Table_Card SET Balance=Balance-@payment WHERE Table_Card.CardID = (Select CardID From inserted)
	PRINT'消费成功'
	end
ELSE
	begin
	PRINT'消费失败'
	Rollback
	end
End


begin Transaction
INSERT INTO Table_Salebill (CardID, MachineID, payamount, saledate) VALUES('C00005', '00000012',10,'2021-5-10');

Commit