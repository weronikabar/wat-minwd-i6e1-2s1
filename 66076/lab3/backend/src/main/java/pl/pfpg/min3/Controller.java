package pl.pfpg.min3;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import pl.pfpg.min3.model.UserQueryResponse;

@RestController
@RequestMapping("/")
@Slf4j
@RequiredArgsConstructor
public class Controller {

  private final GithubService githubService;

  @GetMapping("/userQuery")
  public UserQueryResponse getUsersByUserName(@RequestParam String userName){
    return githubService.getUsersByUserName(userName);
  }

  @GetMapping("/followersGraph")
  public void getFollowers(@RequestParam String userName){
    githubService.getFollowers(userName);
  }
}
