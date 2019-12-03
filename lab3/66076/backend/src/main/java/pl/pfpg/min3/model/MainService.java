package pl.pfpg.min3.model;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

@RequiredArgsConstructor
@Slf4j
@Service
public class MainService {

  public UserInformation getUserData(InputRequest inputRequest) {
    log.info(inputRequest.input);
    log.info(inputRequest.graphDepth);
    return UserInformation.builder().email("piotrek jestem").build();
  }
}
