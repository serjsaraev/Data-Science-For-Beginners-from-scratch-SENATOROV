"""Issues flow."""

# ## Questions
#
# ## Общие вопросы
# - Что такое Issues на GitHub и для чего они используются?
# - Чем Issues отличаются от других инструментов управления задачами?
# - Какие основные компоненты (поля) есть у каждого Issue?
#
# ## Создание Issues
# - Как создать новое Issue в репозитории?
# - Какие данные рекомендуется указывать в описании Issue для лучшего понимания задачи?
# - Какие теги (labels) можно добавить к Issue? Какие из них стандартные?
# - Как прикрепить Assignees (ответственных) к Issue?
#
# ## Работа с Issues
# - Как использовать Labels для классификации задач?
# - Для чего нужен Milestone, и как связать его с Issue?
# - Как привязать Issue к пул-реквесту (Pull Request)?
# - Как добавить комментарий к существующему Issue?
#
# ## Закрытие и завершение Issues
# - Как закрыть Issue вручную?
# - Можно ли автоматически закрыть Issue с помощью сообщения в коммите или пул-реквесте? Как это сделать?
# - Как повторно открыть закрытое Issue, если работа ещё не завершена?
#
# ## Фильтрация и поиск
# - Как найти все открытые или закрытые Issues в репозитории?
# - Как использовать фильтры для поиска Issues по меткам, исполнителям или другим критериям?
# - Как сортировать Issues по приоритету, дате создания или другим параметрам?
#
# ## Интеграции и автоматизация
# - Как настроить автоматические уведомления о новых или изменённых Issues?
# - Что такое Projects в контексте GitHub, и как связать их с Issues?
# - Какие сторонние инструменты можно использовать для автоматизации работы с Issues (например, боты, Webhooks)?
#
# ## Коллаборация
# - Как упомянуть другого пользователя в комментарии к Issue?
# - Как запросить дополнительные данные или уточнения у автора Issue?
# - Что делать, если Issue неактуально или его нужно объединить с другим?
#
# ## Практические аспекты
# - Как использовать шаблоны для создания Issues?
# - Что такое Linked Issues, и как создать связь между задачами?
# - Какие метрики (например, время выполнения) можно отслеживать с помощью Issues?
# - Какие best practices рекомендуются при работе с Issues в команде?
#
#
#

# ## Answers
#
#
# ## General Questions
# - Tracking tool for reporting bugs, requesting features, and managing work in a repository.
# - They integrate directly with GitHub, linking to code, commits, and pull requests.
# - Title, description, labels, assignees, milestones, linked pull requests, comments, relationships, and status.
#
# ## Creating Issues
# - Issues -> New Issue -> Add details -> Create
# - Meaningful title, problem details, expected behavior, reproduction steps, and screenshots.
# - bug, enhancement, question, documentation, help wanted. Labels can be customized.
# - Click on Assignees in the Issue and select a collaborator.
#
# ## Working with Issues
# - Organize Issues in some groups, for example by category, priority, or status.
# - Issues relates to a particular release. Add it via the Milestones section on issue page.
# - Mention #issue-number in the PR description.
# - In the comment section, write comment in input section and click Comment
#
# ## Closing Issues
# - Click Close issue.
# - Yes, use Fixes #issue-number or Closes #issue-number in a commit or PR.
# - Click Reopen issue.
#
# ## Searching Issues
# - Use the Issues tab filters.
# - Use filters like label:bug or assignee:username.
# - Use the Sort dropdown (newest, oldest etc.).
#
# ## Automation & Integration
# - Watch the repository.
# - GitHub Projects are boards for tracking tasks. Issue can be linked to a Project by selecting the project in the Projects section.
# - GitHub Action,
#
# ## Collaboration
# - Use @username in a comment.
# - Comment and mention @username.
# - Close it or link related Issues using #issue-number.
#
# ## Practical Tips
# - Template can be created to standardize issue creation, so every issue is created by following it.
# - Related Issues referenced using #issue-number.
# - Resolution time, open vs. closed Issues, active contributors.
# - Use clear descriptions, labels, and milestones. Close Issues properly.
