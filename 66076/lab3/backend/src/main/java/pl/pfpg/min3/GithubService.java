package pl.pfpg.min3;

import java.io.IOException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.kohsuke.github.GHRepository;
import org.kohsuke.github.GHUser;
import org.kohsuke.github.GHUserSearchBuilder;
import org.kohsuke.github.GitHub;
import org.kohsuke.github.PagedSearchIterable;
import org.springframework.stereotype.Service;


@Service
@RequiredArgsConstructor
@Slf4j
public class GithubService {

  public void test(){
    try {
      GitHub gitHub = GitHub.connectAnonymously();
      GHUserSearchBuilder ghUserSearchBuilder = gitHub.searchUsers();
      PagedSearchIterable<GHUser> list = ghUserSearchBuilder.in("Piotr-Filochowski").list();
      System.out.println("\n\n\n");
      list.forEach(x -> {
        try {
          log.info(x.getEmail());
        } catch (IOException ex) {
          ex.printStackTrace();
        }
      });

    } catch (IOException e) {
      e.printStackTrace();
    }


  }

}
