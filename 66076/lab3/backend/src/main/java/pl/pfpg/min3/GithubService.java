package pl.pfpg.min3;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.kohsuke.github.GHUser;
import org.kohsuke.github.GHUserSearchBuilder;
import org.kohsuke.github.GitHub;
import org.kohsuke.github.PagedSearchIterable;
import org.springframework.stereotype.Service;
import pl.pfpg.min3.model.UserInformation;
import pl.pfpg.min3.model.UserQueryResponse;


@Service
@RequiredArgsConstructor
@Slf4j
public class GithubService {

  public static final String USERS = "Users";

  public UserQueryResponse getUsersByUserName(String userName){
    try {
      GitHub gitHub = GitHub.connectAnonymously();
      GHUserSearchBuilder ghUserSearchBuilder = gitHub.searchUsers();
      PagedSearchIterable<GHUser> list = ghUserSearchBuilder.q(userName).list().withPageSize(15);
      log.info(String.valueOf(list.getTotalCount()));
      UserQueryResponse userQueryResponse = new UserQueryResponse();
      List<UserInformation> users = new ArrayList<>();
      list.forEach(x -> users.add(createUser(x))
      );
      userQueryResponse.setUsers(users);
      return userQueryResponse;
    } catch (IOException e) {
//      log.error(e.getMessage());
      e.printStackTrace();
      return null;
    }
  }

  private UserInformation createUser(GHUser x) {
    try {
      log.info(x.getName());
      return UserInformation.builder().
          email(x.getEmail()).
          name(x.getName()).
          avatarUrl(x.getAvatarUrl()).
          blog(x.getBlog()).
          company(x.getCompany()).
          createdAt(x.getCreatedAt()).
          followersCount(x.getFollowersCount()).
          followingCunt(x.getFollowingCount()).
          build();
    } catch (IOException e) {
      e.printStackTrace();
    }
    return null;
  }

  public void getFollowers(String userName) {
    
  }
}
