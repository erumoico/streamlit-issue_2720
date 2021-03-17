import {
	StreamlitComponentBase,
	withStreamlitConnection
} from "streamlit-component-lib";
import React, { ReactNode } from "react"

/**
 * This is a main component.
 */
class LoremIpsum extends StreamlitComponentBase {
	public render = (): ReactNode => {
		return (
			<div>
				Lorem Ipsum quas reiciendis sit ut. Iusto quibusdam aut eligendi et repellat quo. Repudiandae maiores fugiat qui consectetur eum recusandae. Consequuntur debitis distinctio iste. Dolore sint reiciendis omnis. Nulla rerum quia tempore aut. Doloremque sint voluptates omnis sint velit pariatur earum. Eos impedit quidem voluptatum sed commodi. In aliquam est voluptatem dignissimos. Ea delectus aut laborum. Sint et et tempora quia. Laborum ut illum quidem eos. In numquam repellat iure sit voluptas ex laudantium. Eum eos ad et quas laboriosam distinctio. Non vero vitae iure perspiciatis. Aut assumenda minus est. Voluptas unde qui esse tempora dicta aut soluta. Quas hic molestiae esse minima fugit ducimus animi tempora. Omnis illo et cupiditate. Nihil voluptas sequi molestiae nulla perspiciatis et cum dignissimos. Quae aut sequi et quaerat nesciunt aut ad. Ut dicta animi nihil quos deserunt molestiae magnam alias. Adipisci blanditiis voluptates suscipit quaerat doloribus veniam.
			</div>
		)
	}
}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(LoremIpsum)
