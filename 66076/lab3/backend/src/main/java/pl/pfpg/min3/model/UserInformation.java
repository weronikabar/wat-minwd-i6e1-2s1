package pl.pfpg.min3.model;

import java.io.Serializable;
import java.util.Date;
import lombok.Builder;
import lombok.Getter;
import lombok.Setter;

@Builder
@Getter
@Setter
public class UserInformation implements Serializable {

  String email;
  String name;
  String avatarUrl;
  String blog;
  String company;
  Date createdAt;
  int followersCount;
  int followingCunt;


}
