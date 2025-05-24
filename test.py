def run_online_banking_flow():
  
    # 온라인 뱅킹 및 결제 과정의 시퀀스를 시뮬레이션하는 함수입니다
    # (Enter)는 해당하는 정보를 입력했다는 가정 하에 넘어갑니다
  
    print("\n--- 온라인 뱅킹/결제 시퀀스 시뮬레이션 시작 ---")

    print("\n[User -> Client]: 로그인 정보 입력")
    # 사용자는 클라이언트에 ID와 PW를 입력합니다
    input(">>> 사용자: 로그인 정보를 입력했습니다. (Enter)")

    print("\n[Client -> AppServer]: 로그인 요청 (ID, PW)")
    # 클라이언트는 입력받은 정보를 애플리케이션 서버에 전송합니다
    input(">>> 클라이언트: 로그인 요청을 전송했습니다. (Enter)")

    print("\n[AppServer -> AuthServer]: 인증 요청 (ID, PW)")
    # 애플리케이션 서버는 인증 서버에 인증을 요청합니다
    input(">>> 애플리케이션 서버: 인증 서버에 인증을 요청했습니다. (Enter)")

    print("\n[AuthServer -> DB]: 사용자 정보 조회")
    # 인증 서버는 데이터베이스에서 사용자 정보를 조회합니다
    input(">>> 인증 서버: 데이터베이스에서 사용자 정보를 조회합니다. (Enter)")

    print("\n[DB -->> AuthServer]: 사용자 정보 응답")
    # 데이터베이스는 조회된 사용자 정보를 인증 서버에 응답합니다
    input(">>> 데이터베이스: 사용자 정보를 응답했습니다. (Enter)")

    print("\n[AuthServer -->> AppServer]: 인증 결과 응답")
    # 인증 서버는 인증 결과를 애플리케이션 서버에 응답합니다
    # --- 사용자 입력: 인증 성공/실패 ---
    auth_success_input = input(">>> 인증 서버: 인증에 성공했습니까? (y/n): ").lower()
    auth_success = (auth_success_input == 'y')
    # -------------------------------------

    if auth_success:
        print("\n--- [alt 인증 성공] ---")
        print("[AppServer -->> Client]: 로그인 성공 응답")
        input(">>> 애플리케이션 서버: 로그인 성공 응답을 전송했습니다. (Enter)")

        print("\n[Client -> User]: 로그인 성공 표시 및 계정 접속")
        # 클라이언트는 사용자에게 로그인 성공을 알리고 계정 화면을 표시합니다
        input(">>> 클라이언트: 로그인 성공을 표시했습니다. (Enter)")

        print("\n[User -> Client]: 송금/결제 메뉴 선택")
        # 사용자는 송금 또는 결제 메뉴를 선택합니다
        input(">>> 사용자: 송금/결제 메뉴를 선택했습니다. (Enter)")

        print("\n[Client -> AppServer]: 거래 정보 전송 (수취인, 금액 등)")
        # 클라이언트는 거래에 필요한 정보를 애플리케이션 서버에 전송합니다
        input(">>> 클라이언트: 거래 정보를 전송했습니다. (Enter)")

        print("\n[AppServer -> DB]: 거래 정보 임시 저장")
        # 애플리케이션 서버는 거래 정보를 데이터베이스에 임시 저장합니다
        input(">>> 애플리케이션 서버: 거래 정보를 임시 저장했습니다. (Enter)")

        print("\n[AppServer -> Client]: 거래 내용 확인 요청")
        # 애플리케이션 서버는 클라이언트에게 거래 내용 확인을 요청합니다
        input(">>> 애플리케이션 서버: 거래 내용 확인을 요청했습니다. (Enter)")

        print("\n[Client -> User]: 거래 내용 확인 표시")
        # 클라이언트는 사용자에게 거래 내용을 보여주고 최종 확인을 요청합니다
        input(">>> 클라이언트: 거래 내용을 표시하고 최종 확인을 요청합니다. (Enter)")

        print("\n[User -> Client]: 최종 확인 (예/아니오)")
        # --- 사용자 입력: 최종 확인 ---
        final_confirm_input = input(">>> 사용자: 최종 확인하시겠습니까? ('확인' 또는 '취소' 입력): ").strip()
        # -------------------------------

        print("\n[Client -> AppServer]: 최종 확인 응답")
        # 클라이언트는 사용자의 최종 확인 응답을 애플리케이션 서버에 전송합니다
        input(f">>> 클라이언트: 최종 확인 응답 ('{final_confirm_input}')을 전송했습니다. (Enter)")


        if final_confirm_input == "확인":
            print("\n--- [alt 최종 확인 예] ---")
            print("[AppServer -> PaymentGateway]: 결제 승인 요청")
            # 애플리케이션 서버는 결제사에 결제 승인을 요청합니다
            input(">>> 애플리케이션 서버: 결제사에 결제 승인을 요청했습니다. (Enter)")

            print("\n[PaymentGateway -> Bank]: 자금 이체 요청")
            # 결제사는 은행에 자금 이체를 요청합니다
            input(">>> 결제사: 은행에 자금 이체를 요청했습니다. (Enter)")

            print("\n[Bank -->> PaymentGateway]: 자금 이체 결과 응답")
            # 은행은 자금 이체 결과를 결제사에 응답합니다
            input(">>> 은행: 자금 이체 결과를 응답했습니다. (Enter)")

            print("\n[PaymentGateway -->> AppServer]: 결제 승인 결과 응답")
            # 결제사는 결제 승인 결과를 애플리케이션 서버에 응답합니다
            # --- 사용자 입력: 결제 성공/실패 ---
            payment_success_input = input(">>> 결제사: 결제가 성공했습니까? (y/n): ").lower()
            payment_success = (payment_success_input == 'y')
            # -----------------------------------

            if payment_success:
                print("\n--- [alt 결제 성공] ---")
                print("[AppServer -> DB]: 거래 결과 저장 (성공)")
                input(">>> 애플리케이션 서버: 데이터베이스에 거래 성공 결과를 저장했습니다. (Enter)")
                print("\n[AppServer -->> Client]: 거래 성공 응답")
                input(">>> 애플리케이션 서버: 거래 성공 응답을 전송했습니다. (Enter)")
                print("\n[Client -> User]: 결제 완료 표시 (영수증 등)")
                input(">>> 클라이언트: 결제 완료를 표시했습니다. (Enter)")
            else:
                print("\n--- [else 결제 실패] ---")
                print("[AppServer -> DB]: 거래 결과 저장 (실패)")
                input(">>> 애플리케이션 서버: 데이터베이스에 거래 실패 결과를 저장했습니다. (Enter)")
                print("\n[AppServer -->> Client]: 거래 실패 응답 (오류 메시지)")
                input(">>> 애플리케이션 서버: 거래 실패 응답을 전송했습니다. (Enter)")
                print("\n[Client -> User]: 결제 실패 표시")
                input(">>> 클라이언트: 결제 실패를 표시했습니다. (Enter)")
            print("\n--- [end alt 결제 성공/실패] ---")

            print("\n[AppServer -> Client]: 사용자에게 알림 전송 (성공/실패)")
            input(">>> 애플리케이션 서버: 사용자에게 알림을 전송했습니다. (Enter)")

            print("\n[Client -> User]: 알림 표시")
            input(">>> 클라이언트: 알림을 표시했습니다. (Enter)")

        else: # 최종 확인 "취소"
            print("\n--- [else 최종 확인 아니오] ---")
            print("[AppServer -> DB]: 임시 거래 정보 삭제")
            input(">>> 애플리케이션 서버: 임시 거래 정보를 삭제했습니다. (Enter)")
            print("\n[AppServer -->> Client]: 거래 취소 응답")
            input(">>> 애플리케이션 서버: 거래 취소 응답을 전송했습니다. (Enter)")
            print("\n[Client -> User]: 거래 취소 표시")
            input(">>> 클라이언트: 거래 취소를 표시했습니다. (Enter)")
        print("\n--- [end alt 최종 확인 예/아니오] ---")

    else: # 인증 실패
        print("\n--- [else 인증 실패] ---")
        print("[AppServer -->> Client]: 로그인 실패 응답 (오류 메시지)")
        input(">>> 애플리케이션 서버: 로그인 실패 응답을 전송했습니다. (Enter)")

        print("\n[Client -> User]: 로그인 실패 표시")
        input(">>> 클라이언트: 로그인 실패를 표시했습니다. (Enter)")
    print("\n--- [end alt 인증 성공/실패] ---")


    print("\n[Client -> User]: 세션 종료 또는 추가 작업 대기")
    input(">>> 클라이언트: 세션 종료 또는 추가 작업 대기 상태입니다. (Enter)")

    print("\n--- 온라인 뱅킹/결제 시퀀스 시뮬레이션 종료 ---")

# 프로그램 시작 지점
if __name__ == "__main__":
    run_online_banking_flow()