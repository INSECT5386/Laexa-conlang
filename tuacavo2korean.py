{
    "Z": {
        "type": "slot tag",
        "meaning": "현재 상황 / 현상"
    },
    "T": {
        "type": "slot tag",
        "meaning": "시간 / 흐름",
        "example": "T1400 -> 14시00분(절대 시간), TdR3h -> 3시간 동안 지속, Tei -> 영구적 상태"
    },
    "K": {
        "type": "slot tag",
        "meaning": "원인 / 전제"
    },
    "F": {
        "type": "slot tag",
        "meaning": "결과 / 작용"
    },
    "N": {
        "type": "slot tag",
        "meaning": "생각 / 가치 판단"
    },
    "Im": {
        "type": "id tag",
        "meaning": "화자 (나)",
        "example": "ImAa -> 임애/내가 조작한다."
    },
    "Ym": {
        "type": "id tag",
        "meaning": "청자 (너)",
        "example": "YmAa -> 윰애/너가 조작한다."
    },
    "Om": {
        "type": "id tag",
        "meaning": "제3자/외부 객체",
        "example": "OmAa ->  씀애/누군가가 조작한다."
    },
    "Logic_Gates": {
        "a'- ": {
            "meaning":"인과관계의 흐름 (A 때문에 B가 됨). / >"
        },
        " aya ": "상호 영향 (A와 B가 서로 주고받음) / <>",
        "sa'- ": {
            "meaning": "지연된 인과 (A가 시간이 흐른 뒤 B를 유발함) / ~>"
        },
        " | ": "a 혹은 b 중 하나. 예시: A|B. / A so B.에이 소 비",
        " en ": "동시 발생 (A와 B가 동시에 일어남). / =",
        " ! ": "즉각적인 대응이 필요한 데이터 (경고/위험).",
        " ? ": "데이터 확인 및 정보 탐색 요청 (질문).",
        " , ": "나열 및 병렬 처리",
        " Eth ": "데이터의 목적 및 성격 규정 (꼬리표). / ;",
        " no ": "부정 (Not/None) / ~",
        " R ": "A는 B이다. / :"
    },
    "Vector_Tags": {
        "Pu": "확장, 상승, 강화",
        "Mu": "축소, 하락, 약화",
        "Cu": "반전, 모순, 거부 (행동에서는 소극성) / Cu.큐",
        "Xu": "설명하기 힘든 모호한 상태 / Xu.쑤",
        "Su": "적극적, 물리적 강화 / Su.수",
        "Ju": "반복, 루프. /Jyu.쥬",
        "Hu": "효율적, 기계적 수행 / Hu.후",
        "Ru": "거칠음/불규칙",
        "Lu": "투명함/명확함",
        "Vu": "취약함/불안정"
    },
    "Number": {
        "example": "T1412 -> 트 외세외테 / Ra50Pu -> 라 네제푸",
        "0": "Ze",
        "1": "Oe",
        "2": "Te",
        "3": "Fe",
        "4": "Se",
        "5": "Ne",
        "6": "Ge",
        "7": "Le",
        "8": "Me",
        "9": "Ka"
    },
    "Vector_Suffix_Extension": {
        "[(1~5) × 10 + (1~5)]": {
            "setting": "지속성은 10의 자리(1: 10분 미만, 2: 30분 미만 및 10분 이상, 3: 1시간 미만 및 30분 이상, 4: 3시간 미만 및 1시간 이상  5: 3시간 이상), 변동성은 1의 자리(1: 안정적, 2: 불안한, 3: 불안정한, 4: 빠름, 5: 매우 빠름).",
            "example": "Ra50Pu -> 고강도 분노가 매우 오래 지속됨. (라네제푸)"
        },
        "@": "대상 지정 (Target) / tu.투"
    },
    "Scope_Tags": {
        "()": "내부, 본질, 비공개 데이터 (내면) / ( : nar.나르, ) : mr.므르",
        "[]": "외부, 표면, 공개 데이터 (행동) / [ : nor.노르, ] : nr.느르",
        "Md": "경계, 필터링 지점 / mor.모르",
        "{}": "논리적 그룹핑 / { : uir.의르, } : ur 우르"
    },
    "Certainy_Tags": {
        "ic": "확정된, 진리",
        "ec": "가변적인, 추측"
    },
    "Primary_Categories": {
        "Va": "결핍/필요 (Vab:육체, Vam:정신, Var:물리)",
        "La": "인지/지식 (Lam:기억, Lai:정보입력, Lac:추론, Lav:확인완료)",
        "Lia": "정보 및 데이터 (Liad : 수치 데이터, Liat: 텍스트/언어 정보, Liam: 미디어/시작 정보",
        "Ka": "충돌/대립, 오류",
        "Sa": "해소/획득 (Sab:육체, Sam:정신, Sar:물리)",
        "Dg": "위계/상급자",
        "Suba": "하위/객체",
        "Pa": "규칙/계약",
        "Za": "평온/수용 (Zas:휴식, Zaa(Zoe) 동의, Zaf:충족)",
        "Ra": "분노/거부 (Rai:짜증, Raf:공포, Ras:슬픔)",
        "Coa": "협력/협동",
        "Ata": "조언/지도",
        "Ta": "신뢰/유대",
        "Exa": "교환/거래",
        "Fa": {
            "meaning": "해상도",
            "derivation":{
                "Fam": "집중"
            }
        },
        "Ena": {
            "meaning": "에너지",
            "derivation":{
                "Enab": "활력"
            }
        },
        "Mita": {
            "meaning": "의지",
            "derivation": {
                "Mitam": "도덕",
                "Mitat": "의도/목적",
                "Mitar": "의욕/사기"
            }
        },
        "Aca": {
            "meaning": "행위 / 행동",
            "derivation": {
                "Ae": {
                    "meaning": "물리적 행동 (Physical Action)",
                    "derivation":{
                        "Aeg": "이동",
                        "Aete": "교육",
                        "Aewa": "대기(어떤 현상이나 상태가 나타나기를 준비하며 머무르는 행위)",
                        "Aeta": "사육",
                        "Aefo": "수리",
                        "Aef": "비행(하늘을 날다)",
                        "Aep": "여가 활동",
                        "Aeup": "가압(힘이나 압력을 가하다)",
                        "Aec": "폐쇠(통로를 차단하거나 공간을 밀봉함)",
                        "Aes": "빠른 이동/질주",
                        "Aet": "투척",
                        "Aek": "보살핌",
                        "Aeir":"조력/지원",
                        "Aegr": "추종/추적",
                        "Aetir": "모방",
                        "Aetu": "주입",
                        "Aelu": "낙하",
                        "Aei": "도약(바닥을 치고 솟구치다(=점프))",
                        "Aeal": "음용(액체를 입을 통해 몸 안으로 들이다)",
                        "Aem": "대면",
                        "Aema": "제작",
                        "Aetou": "접촉",
                        "Aer": "섭취",
                        "Aeze": "수령(외부에서 오는 물건이나 신호를 내 쪽으로 받아들이는 행위)",
                        "Aelo": "시청/관찰",
                        "Aebo": "파괴",
                        "Aeop": "기립(아래에 있던 몸을 일으켜 세우는 동작(=일어서다))",
                        "Aeso": "은폐/잠적",
                        "Aelit": "휴식",
                        "Aetur": "식재(나무나 풀을 땅에 박아 넣는 행위)",
                        "Aeur": "착석",
                        "Aeun": "비존재",
                        "Aein": "존재",
                        "Aecr": "개방(통로를 열거나 밀봉을 품)",
                        "Aeol": "착용",
                        "Aesl": "취침",
                        "Aekir": "성장",
                        "Aeku": "절단",
                        "Aeca": "파지(물건을 손에 쥐고 놓치지 않게 유지하는 행위)",
                        "Aeki": "제공",
                        "Aeba": "사망",
                        "Aena": "생존",
                        "Aetat": "포획/검거"
                    }
                },
                "Au": {
                    "meaning": "언어적 행위",
                    "derivation":{
                        "Ausi": "발화(심리적인 생각이나 언어를 입 밖으로 내어 소리를 내는 물리적 행위)",
                        "Aues": "독해",
                        "Auer": "작성",
                        "Auli": "청취",
                        "Aulo": "고성(목소리를 높여 크게 소리를 냄.)",
                        "Auls": "귓속말",
                        "Aulc": "의사소통",
                        "Ausk": "질문"
                    }
                },
                "Aa": "조작 및 제어 (Manipulation)"
            }
        },
        "Eg": {
            "meaning": "환경/객체",
            "derivation": {
                "Ec": {
                    "meaning": "위치/장소 / Ec.에곡",
                    "derivation": {
                        "Eco": {
                            "meaning": "장애물/방해 요소"
                        },
                        "Ecu": {
                            "meaning": "안전 구역/안전 시설",
                            "derivation": {
                                "Ecuo": "집",
                                "Ecup": "경찰서",
                                "Ecuf": "소방서"
                            }
                        },
                        "Eca": {
                            "meaning": "교육 시설",
                            "derivation": {
                                "Ecas": {
                                    "meaning": "학교",
                                    "derivation":{
                                        "Secas": "초등학교",
                                        "Mecas": "중학교",
                                        "Hecas": "고등학교",
                                        "Uecas": "대학교",
                                        "Cecas": "사립학교"
                                    }
                                },
                                "Ecaa": {
                                    "meaning": "학원",
                                    "derivation":{
                                        "Uecaa": "대학원"
                                    }
                                },
                                "Ecata": "대학교"
                            }
                        },
                        "Ece": {
                            "meaning": "공공 시설",
                            "derivation":{
                                "Eceg": "공원",
                                "Eceb": "벤치/정자",
                                "Ecep": "놀이터",
                                "Ecegb": "놀이공원 / Ekyegb.에켹브",
                                "Eceu": "산책로",
                                "Ecenv": "화장실 / Ekyenv.에켼브"
                            }
                        },
                        "Ecei": {
                            "meaning": "산업 시설",
                            "derivation":{
                                "Eceic": "회사",
                                "Eceif": "생산 시설/공장",
                                "Eceir": "사무실"
                            }
                        },
                        "Ecea": {
                            "meaning": "상업 시설",
                            "derivation": {
                                "Eceam": "마트/시장",
                                "Eceas": "상점/편의점",
                                "Ecear": "식당",
                                "Eceaf": "카페"
                            }
                        },
                        "Echi": {
                            "meaning": "의료/복지 시설",
                            "derivation":{
                                "Echip": "병원",
                                "Echiu": "복지관/요양 시설"
                            }
                        }
                    }
                },
                "Egob": "사물/도구 / Egob.에곱",
                "Egev": "환경 조건(날씨, 온도, 조명 등) / Egev.에겝",
                "Exi": "시스템/프로세스 (기계적 절차) / Egsy.엑시"
            }
        },
        "Pin": {
            "meaning": "실행/계획",
            "derivation":{
                "hold": "일시 중단/보류 / hold. 홀드",
                "run": "-중 이다 / run.런",
                "end": "-했다. / end.엔드",
                "now": "하다",
                "utur": "할 것 이다."
            }
        },
        "Val": "가치 존재",
        "Has": "소유/연결"
    },
    "fitr": {
        "#Burnout": "{Tef + KaRHigh + (RaPu)}",
        "#Flow": "{Tef + Lac + (ZafPu)}"
    },
    "Humanity_Tags": {
        "eta": "비논리적 직관",
        "ata": "공감/상태 공유",
        "uta": "상상/가능성"
    },
    "Examples": {
        "{ImAegrun} @Ym": "나는 너에게 가는 중이다.",
        "{ImAegend @Eceaf} a'{ImAemend @Ym}, ImAulcnow @Ym": "나는 카페에 도착해서 너를 만났고, 너에게 말하고 있다.",
        "{{ImAegnow} en {YmAegnow}} 'a{ImAemnow @Ym}": "나는 이동하다. 너도 이동하다. 그로인해, 나는 너를 대면하다."
    },
    "GlobalSettings": {
        "meaning": "전체적 설정. 언어의 규칙 정의.",
        "N1": {
            "setting": "Scope_Tags는 문장의 끝부분에서는 생략 가능."
        },
        "N2": {
            "setting": "aa는 ae로 발음.",
            "example": {"Zaa": "Zae(=재)"}
        },
        "N3": {
            "setting": "C는 Ky로 발음."
        },
        "N4": {
            "setting": "J는 Jy로 발음.",
            "example": {"Ju": "Jyu(=쥬)"}
        }
    }
}
