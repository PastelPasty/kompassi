import Link from "next/link";
import { notFound } from "next/navigation";

import { Fragment } from "react";
import { markAsFavorite, unmarkAsFavorite } from "../../program/actions";
import FavoriteButton from "../../program/FavoriteButton";
import { FavoriteContextProvider } from "../../program/FavoriteContext";
import { graphql } from "@/__generated__";
import { ProgramLinkType } from "@/__generated__/graphql";
import { getClient } from "@/apolloClient";
import FormattedDateTimeRange from "@/components/FormattedDateTimeRange";
import { validateFields } from "@/components/forms/models";
import { SchemaForm } from "@/components/forms/SchemaForm";
import SubmitButton from "@/components/forms/SubmitButton";
import Linebreaks from "@/components/helpers/Linebreaks";
import Paragraphs from "@/components/helpers/Paragraphs";
import ParagraphsDangerousHtml from "@/components/helpers/ParagraphsDangerousHtml";
import ViewContainer from "@/components/ViewContainer";
import ViewHeading from "@/components/ViewHeading";
import getPageTitle from "@/helpers/getPageTitle";
import { getTranslations } from "@/translations";

const query = graphql(`
  query ProgramDetailQuery(
    $eventSlug: String!
    $programSlug: String!
    $locale: String
  ) {
    profile {
      program {
        programs(eventSlug: $eventSlug) {
          slug
        }
      }
    }

    event(slug: $eventSlug) {
      name
      program {
        calendarExportLink
        program(slug: $programSlug) {
          title
          description
          cachedHosts

          links(lang: $locale) {
            type
            href
            title
          }

          dimensions {
            dimension {
              slug
              title(lang: $locale)
            }
            value {
              slug
              title(lang: $locale)
            }
          }
          scheduleItems {
            startTime
            endTime
          }
        }
      }
    }
  }
`);

interface Props {
  params: {
    locale: string;
    eventSlug: string;
    programSlug: string;
  };
}

export const revalidate = 5;

export async function generateMetadata({ params }: Props) {
  const { locale, eventSlug, programSlug } = params;
  const translations = getTranslations(locale);
  const { data } = await getClient().query({
    query,
    variables: { eventSlug, programSlug, locale },
  });
  const title = getPageTitle({
    translations,
    event: data.event,
    viewTitle: translations.Program.singleTitle,
    subject: data?.event?.program?.program?.title,
  });
  const description = data?.event?.program?.program?.description;
  return { title, description };
}

function getLinkEmoji(type: ProgramLinkType) {
  switch (type) {
    case ProgramLinkType.Calendar:
      return "📅";
    case ProgramLinkType.Signup:
      return "✍️";
    case ProgramLinkType.Feedback:
      return "📝";
    case ProgramLinkType.Recording:
      return "🎥";
    case ProgramLinkType.Remote:
      return "🌐";
    case ProgramLinkType.Reservation:
    case ProgramLinkType.Tickets:
      return "🎟️";
    case ProgramLinkType.Other:
    default:
      return "🔗";
  }
}

export default async function NewProgramPage({ params }: Props) {
  const { locale, eventSlug, programSlug } = params;
  const translations = getTranslations(locale);
  const t = translations.Program;
  const { data } = await getClient().query({
    query,
    variables: { eventSlug, programSlug, locale },
  });
  const { event } = data;
  if (!event?.program?.program) {
    notFound();
  }

  const program = event.program.program;
  const favoriteProgramSlugs =
    data.profile?.program?.programs?.map((program) => program.slug) ?? [];

  // TODO make configurable which dimensions to show
  const dimensions = program.dimensions.filter(
    (dimension) => dimension.dimension.slug !== "date",
  );

  return (
    <ViewContainer>
      <Link className="link-subtle" href={`/events/${eventSlug}/program`}>
        &lt; {t.actions.returnToProgramList}
      </Link>

      <ViewHeading>
        {program.title}
        <ViewHeading.Sub>{t.inEvent(event.name)}</ViewHeading.Sub>
        {data.profile && (
          <div className="d-inline-block ms-2">
            <FavoriteContextProvider
              slugs={favoriteProgramSlugs}
              messages={t.favorites}
              markAsFavorite={markAsFavorite.bind(null, locale, eventSlug)}
              unmarkAsFavorite={unmarkAsFavorite.bind(null, locale, eventSlug)}
            >
              <FavoriteButton slug={programSlug} size="xl" />
            </FavoriteContextProvider>
          </div>
        )}
      </ViewHeading>

      <p className="fst-italic">
        {program.scheduleItems.map((scheduleItem, index) => (
          <FormattedDateTimeRange
            locale={locale}
            scope={event}
            session={null}
            key={index}
            start={scheduleItem.startTime}
            end={scheduleItem.endTime}
            includeDuration={true}
          />
        ))}
        {program.cachedHosts && (
          <>
            {", "}
            {program.cachedHosts}
          </>
        )}
      </p>

      <div className="mb-3 mt-3">
        {program.links.map((link, index) => (
          <div key={index}>
            <a
              href={link.href}
              target="_blank"
              rel="noopener noreferrer"
              className="link-subtle"
            >
              {getLinkEmoji(link.type) + " "}
              {link.title}…
            </a>
          </div>
        ))}
      </div>

      <div className="mb-3 mt-3">
        {dimensions.map((dimension) => (
          <div key={dimension.dimension.slug}>
            <strong>{dimension.dimension.title}</strong>:{" "}
            {dimension.value.title}
          </div>
        ))}
      </div>

      <article className="mb-3">
        <Paragraphs text={program.description} />
      </article>
    </ViewContainer>
  );
}
