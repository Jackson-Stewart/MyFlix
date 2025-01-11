FROM nginx:alpine

# Install AWS CLI
RUN apk add --no-cache aws-cli

# Set working directory
WORKDIR /app

# Create and set permissions for videos directory
RUN mkdir -p /app/videos && \
    chown -R nginx:nginx /app/videos && \
    chmod -R 755 /app/videos

# Copy application files
COPY . .

# Copy nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Set proper ownership for all files
RUN chown -R nginx:nginx /app && \
    chmod -R 755 /app

EXPOSE 3001

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
